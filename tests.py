import unittest
import httpx
import xkcd


class Tests(unittest.TestCase):
    def test_latest(self):
        latest_xkcd = client.latest()
        latest = httpx.get("https://xkcd.com/info.0.json").json()
        self.assertEqual(latest_xkcd.num, latest["num"])

    def test_get(self):
        latest_xkcd = client.latest()
        latest = client.get(latest_xkcd.num)
        self.assertEqual(latest_xkcd.num, latest.num)

    def test_random(self):
        random_xkcd = client.random()
        xkcd = client.get(random_xkcd.num)
        self.assertEqual(random_xkcd.num, xkcd.num)

    def test_response(self):
        latest_xkcd = client.latest()
        other_xkcd = client.random()
        self.assertNotEqual(latest_xkcd, other_xkcd)

        xkcd1 = client.get(1)  # hardcoded test case
        resp = xkcd.Response(xkcd1.raw())
        self.assertEqual(xkcd1, resp)


if __name__ == "__main__":
    client = xkcd.Client()
    unittest.main()
