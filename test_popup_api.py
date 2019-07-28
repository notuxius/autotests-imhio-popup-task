import pytest
import requests


# Methods that are used in API tests:
def _make_post_receive_response(url_port_endp, user_action, feedback):
    return requests.post(url_port_endp, json={"user_action": user_action, "feedback": feedback})


# API Tests:
@pytest.mark.parametrize("user_action, feedback", [("0", 'Testing API valid "0" user action ~!@#$%^&*()_+{}|:<>?,./;\'[]\\|=-`'),
                                                   ("1", 'Testing API valid "1" user action'),
                                                   ("2", 'Testing API valid "2" user action'),
                                                   ("3", 'Testing API valid "3" user action'),
                                                   ("4", 'Testing API valid "4" user action'),
                                                   ("5", 'Testing API valid "5" user action'),
                                                   ("6", 'Testing API valid "6" user action'),
                                                   ("7", ""),
                                                   ("8", ""),
                                                   ("9", ""),
                                                   ("10", "")])
def test_valid_user_action(url_port_endp, user_action, feedback):
    resp = _make_post_receive_response(url_port_endp[0], user_action, feedback)
    assert resp.status_code == 200


@pytest.mark.parametrize("user_action, feedback", [("-1", 'Testing API inval "-1" user action'),
                                                   ("11", 'Testing API inval "11" user action')])
def test_inval_user_action(url_port_endp, user_action, feedback):
    resp = _make_post_receive_response(url_port_endp[0], user_action, feedback)
    assert resp.status_code == 400


@pytest.mark.parametrize("user_action, feedback", [("", "Testing API empty user action")])
def test_inval_empty_user_action(url_port_endp, user_action, feedback):
    resp = _make_post_receive_response(url_port_endp[0], user_action, feedback)
    assert resp.status_code == 400


@pytest.mark.parametrize("user_action, feedback", [("5", "Testing API inval endpoint")])
def test_inval_endp(url_port_endp, user_action, feedback):
    resp = _make_post_receive_response(url_port_endp[1], user_action, feedback)
    assert resp.status_code == 404


@pytest.mark.parametrize("user_action, feedback", [("5", "Testing API empty endpoint")])
def test_inval_empty_endp(url_port_endp, user_action, feedback):
    resp = _make_post_receive_response(url_port_endp[2], user_action, feedback)
    assert resp.status_code == 404


@pytest.mark.parametrize("user_action, feedback", [("5", "Testing API too long feedback Testing too long feedback \
Testing too long feedback Testing too long feedback Testing too long feedback Testing too long feedback \
Testing too long feedback Testing too long feedback Testing too long feedback Testing too long feedback")])
def test_inval_too_long_feedback(url_port_endp, user_action, feedback):
    resp = _make_post_receive_response(url_port_endp[0], user_action, feedback)
    assert resp.status_code == 400


@pytest.mark.parametrize("user_action, feedback", [("7", "Testing API non empty feedback user action greater than 6")])
def test_inval_non_empty_feedback_user_action_gt_6(url_port_endp, user_action, feedback):
    resp = _make_post_receive_response(url_port_endp[0], user_action, feedback)
    assert resp.status_code == 400


@pytest.mark.parametrize("user_action, feedback", [("5", "Testing API not JSON request")])
def test_inval_not_json_request(url_port_endp, user_action, feedback):
    xml = """<?xml version='1.0' encoding='utf-8'?>
    <a>01</a>"""
    headers = {'Content-Type': 'application/xml'}
    resp = requests.post(url_port_endp[0], data=xml, headers=headers)
    assert resp.status_code == 400


# @pytest.mark.parametrize("user_action, feedback", [("5", "Testing API invalid method")])
# def test_inval_method(url_port_endp, user_action, feedback):
#     resp = requests.get(url_port_endp[0], json={"user_action": user_action, "feedback": feedback})
#     resp = requests.put(url_port_endp[0], json={"user_action": user_action, "feedback": feedback})
#     resp = requests.delete(url_port_endp[0], json={"user_action": user_action, "feedback": feedback})
#     assert resp.status_code == 400
