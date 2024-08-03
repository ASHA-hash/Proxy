
from twocaptcha import TwoCaptcha


def solveRecaptcha(sitekey, url):
    api_key = "46d1477957abf0d7360f4ee4cc140873"

    solver = TwoCaptcha(api_key)


    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url)

    except Exception as e:
        print(e)

    else:
        return result