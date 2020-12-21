import os

pytest_plugins = 'pytester'


def test_aioresponses(testdir):
    testdir.makeconftest(open(os.path.dirname(__file__) + '/pytest_aioresponses.py').read())
    testdir.makepyfile(
        """
        import pytest
        import aiohttp

        @pytest.mark.asyncio
        async def test_something(aioresponses):
            aioresponses.get("https://hello.aio")

            async with aiohttp.ClientSession() as session:
                async with session.get("https://hello.aio") as response:
                    assert response.status == 200
    """
    )

    # run all tests with pytest
    result = testdir.runpytest()

    # check that all 4 tests passed
    result.assert_outcomes(passed=1)
