from actionnetwork import action_network as an
from faker import Faker
import responses
from responses import matchers
import pytest
import secrets
from urllib.parse import urljoin

fake = Faker()


@pytest.fixture
def main_api_key():
    return secrets.token_hex(16)


@pytest.fixture
def people_endpoint():
    return "https://actionnetwork.org/api/v2/people"


@responses.activate
def test_correct_api_key(settings, main_api_key, people_endpoint):
    settings.ACTIONNETWORK_API_KEYS = {"main": main_api_key}
    url = "https://actionnetwork.org/api/v2/people"
    responses.add(
        responses.GET,
        url=people_endpoint,
        status=200,
        match=[matchers.header_matcher({"OSDI-API-Token": main_api_key})],
    )
    assert an.call_api(url).status_code == 200


@responses.activate
def test_missing_api_key(settings, people_endpoint):
    settings.ACTIONNETWORK_API_KEYS = {"main": secrets.token_hex(16)}
    responses.add(
        responses.GET,
        url=people_endpoint,
        status=403,
    )
    assert an.call_api(people_endpoint).status_code == 403


@responses.activate
def test_people_from_email(faker, people_endpoint):
    email = faker.email()
    responses.add(
        responses.GET,
        url=people_endpoint,
        match=[matchers.query_param_matcher({"filter": f"email_address eq '{email}'"})],
        json={"_links": {"osdi:people": [{"href": people_endpoint + faker.uuid4()}]}},
        status=200,
    )
    assert len(an.People(email=email).ids) > 0


@responses.activate
def test_taggings_has_tag(faker):
    voting_member_tag_id = faker.uuid4()
    person_uuid = faker.uuid4()
    assert voting_member_tag_id != person_uuid
    responses.add(
        responses.GET,
        url=f"https://actionnetwork.org/api/v2/people/{person_uuid}/taggings",
        json={
            "_embedded": {
                "osdi:taggings": [
                    {
                        "_links": {
                            "osdi:tag": {
                                "href": f"https://actionnetwork.org/api/v2/tags/{voting_member_tag_id}"
                            }
                        }
                    }
                ]
            }
        },
    )
    taggings = an.Taggings(person_uuid)
    assert voting_member_tag_id in taggings.tags


def test_uuid(faker):
    uuid = faker.uuid4()
    assert an.Person(uuid).uuid == uuid


@responses.activate
def test_person_from_people(faker):
    person1_endpoint = f"https://actionnetwork.org/api/v2/people/{faker.uuid4()}"
    responses.add(responses.GET, person1_endpoint, json={})
    people = an.People({"_links": {"osdi:people": [{"href": person1_endpoint}]}})
    assert an.Person.first_from_people(people) is None


@responses.activate
def test_people_init(faker, people_endpoint):
    uuid = faker.uuid4()
    responses.add(
        responses.GET,
        people_endpoint,
        status=200,
        json={"_links": {"osdi:people": [{"href": urljoin(people_endpoint, uuid)}]}},
    )
    assert an.People().ids == [uuid]


def test_tag_json():
    assert an.Tag({}).json == {}


def test_get_tag_from_uuid(faker, monkeypatch):
    uuid = faker.uuid4()
    monkeypatch.setattr(
        an, "call_api", lambda uri: {"identifiers": ["action_network:" + uuid]}
    )
    tag = an.Tag.from_uuid(uuid).json
    assert tag["identifiers"][0].split(":")[1] == uuid


@responses.activate
def test_dsa_member_status(faker):
    uuid = faker.uuid4()
    responses.add(
        responses.GET,
        url=f"https://actionnetwork.org/api/v2/people/{uuid}",
        json={"custom_fields": {"DSA Member Status": "member in good standing"}},
    )
    assert (
        an.Person(uuid).custom_fields["DSA Member Status"] == "member in good standing"
    )
