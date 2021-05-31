# -*- coding: UTF-8 -*-

from linkv_sdk import linkv_sdk


def main():
    app_id = ''
    app_secret = ''
    if not linkv_sdk.init(app_id, app_secret):
        return

    rtc = linkv_sdk.LvRTC()

    print(rtc.GenAuth())


if __name__ == "__main__":
    main()