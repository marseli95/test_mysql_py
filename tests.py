from unittest import mock
from app import run_q

@mock.patch('app.exec_mysql')
def test_run_q(mysql_mock):
    run_q()
    mysql_mock.assert_called_with('blahblahblah')