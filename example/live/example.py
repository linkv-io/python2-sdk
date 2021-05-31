# -*- coding: UTF-8 -*-

from linkv_sdk import linkv_sdk


def main():
    app_id = ''
    app_secret = ''

    if not linkv_sdk.init(app_id, app_secret):
        return

    live = linkv_sdk.LvLIVE()

    third_uid = "test-py-tob"
    a_id = "test"
    r = live.GetTokenByThirdUID(third_uid, a_id, user_name='test-py', sex=linkv_sdk.SexTypeUnknown,
                                portrait_uri='http://xxx.xx.xxx/app/rank-list/static/img/defaultavatar.cd935fdb.png')

    if not r['status']:
        print('live.GetTokenByThirdUID(%s)' % r['error'])
        return

    print('token:%s' % r['live_token'])
    live_open_id = r['live_open_id']
    r1 = live.GetGoldByLiveOpenID(live_open_id)
    if not r1['status']:
        print('live.GetGoldByLiveOpenID(%s)' % r1['error'])
        return
    golds0 = r1['golds']
    print('golds0:%d' % golds0)
    order_id = ''
    gold = 10
    r2 = live.SuccessOrderByLiveOpenID(live_open_id, linkv_sdk.OrderTypeAdd, gold, 10, 1,
                                       linkv_sdk.PlatformTypeH5, order_id)
    if not r2['status']:
        print('live.SuccessOrderByLiveOpenID(%s)' % r2['error'])
        return

    golds1 = r2['golds']
    print('golds1:%d' % golds1)
    if (gold + golds0) != golds1:
        print('(golds0+gold) != golds1')
        return

    ok = live.ChangeGoldByLiveOpenID(live_open_id, linkv_sdk.OrderTypeDel, gold, 1, 'test del')
    if not ok:
        print('!ok')
        return

    r3 = live.GetGoldByLiveOpenID(live_open_id)
    if not r3['status']:
        print('live.GetGoldByLiveOpenID(%s)' % r3['error'])
        return
    golds2 = r3['golds']
    print('golds2:%d' % golds2)

    if golds0 != golds2:
        print('golds0 != golds2')

    print('success')


if __name__ == "__main__":
    main()
