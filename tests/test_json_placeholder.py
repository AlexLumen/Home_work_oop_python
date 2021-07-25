import pytest
import requests
import cerberus
import random
from allpairspy import AllPairs
from data.placeholder_schema import post_schema


@pytest.mark.parametrize("title, body, user_id", [
    items for items in AllPairs([
        ["New_post", "Новый пост", "New_post!@test.com", ""],
        ["Bar post", "Тело поста", "!@#$^&*()123456789+=-_0{}[]:;'?/|", ""],
        [1, 5, 10]
    ])
])
def test_post_post(base_url_placeholder_api, title, body, user_id):
    """Check CREATE POSTS api"""
    url = f'{base_url_placeholder_api}/posts'
    res = requests.post(url=url,
                        data={'title': title, 'body': body, 'userId': user_id})
    res_json = res.json()
    assert res.status_code == 201, "Incorrect code"
    assert 'id' in res_json, "no post id"
    assert res_json['userId'] == str(user_id), "Incorrect user id"
    assert res_json['title'] == title, "Incorrect title"
    assert res_json['body'] == body, "Incorrect body"


def test_get_post_by_id(base_url_placeholder_api):
    """Check GET POSTS BY ID api"""
    post_id = random.randint(1, 10)
    res = requests.get(f'{base_url_placeholder_api}/posts/{post_id}')
    res_json = res.json()
    v = cerberus.Validator()
    assert res.status_code == 200, "Incorrect code"
    assert post_id == res_json['id'], "Incorrect id"
    assert v.validate(res.json(), post_schema)


@pytest.mark.parametrize('completed_state', [False, True])
def test_get_todos(base_url_placeholder_api, completed_state):
    """Check GET TODOS api"""
    user_id = random.randint(1, 10)
    url = f'{base_url_placeholder_api}/todos?userId={user_id}&completed={completed_state}'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 200, "Incorrect code"
    for item in range(len(res_json)):
        assert user_id == res_json[item]["userId"], "Incorrect user id"
        assert completed_state == res_json[item]["completed"], "Incorrect title"


def test_404_method_get_posts(base_url_placeholder_api):
    """Check 404 code BY POST NON-EXISTENT ID api"""
    post_id = 1005009090
    res = requests.get(f'{base_url_placeholder_api}/posts/{post_id}')
    res_json = res.json()
    assert res.status_code == 404, "Incorrect code"
    assert res_json == {}, "dictionary is not empty"


@pytest.mark.parametrize("title, body, user_id, post_id", [
    items for items in AllPairs([
        ["Edit_post", "Отредактированный  пост", "Edit_post!@test.com", ""],
        ["New Bar post", "Новое тело поста", "!@#$^&*()123456789+=-_0{}[]:;'?/|", ""],
        [1, 5, 10],
        [1, 9, 7]
    ])
])
def test_put_post(base_url_placeholder_api, title, body, user_id, post_id):
    """Check PUT POSTS api"""
    url = f'{base_url_placeholder_api}/posts/{post_id}'
    res = requests.put(url=url,
                       data={'title': title, 'body': body, 'userId': user_id})
    res_json = res.json()
    assert res.status_code == 200, "Incorrect code"
    assert res_json['id'] == post_id, "no post id"
    assert res_json['userId'] == str(user_id), "Incorrect user id"
    assert res_json['title'] == title, "Incorrect title"
    assert res_json['body'] == body, "Incorrect body"
