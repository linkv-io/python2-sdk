# -*- coding: UTF-8 -*-

from linkv_sdk import linkv_sdk


def main():
    app_id = 'rbaiHjNHQyVprPCBSHevvVvuNynNeTvp'
    app_secret = '87EA975D424238D0A08F772321169816DD016667D5BB577EBAEB820516698416E4F94C28CB55E9FD8E010260E6C8A177C0B078FC098BCF2E9E7D4A9A71BF1EF8FBE49E05E5FC5A6A35C6550592C1DB96DF83F758EAFBC5B342D5D04C9D92B1A82A76E3756E83A4466DA22635A8A9F88901631B5BBBABC8A94577D66E8B000F4B179DA99BAA5E674E4F793D9E60EEF1C3B757006459ABB5E6315E370461EBC8E6B0A7523CA0032D33B5C0CF83264C9D83517C1C94CAB3F48B8D5062F5569D9793982455277C16F183DAE7B6C271F930A160A6CF07139712A9D3ABF85E05F8721B8BB6CAC1C23980227A1D5F31D23FA6567578AEEB6B124AF8FF76040F9598DDC9DE0DA44EF34BBB01B53E2B4713D2D701A9F913BE56F9F5B9B7D8D2006CA910D8BFA0C34C619AB0EEBDAA474E67115532511686992E88C4E32E86D82736B2FE141E9037381757ED02C7D82CA8FC9245700040D7E1E200029416295D891D388D69AC5197A65121B60D42040393FB42BC2769B1E2F649A7A17083F6AB2B1BE6E993'

    if not linkv_sdk.init(app_id, app_secret):
        return

    live = linkv_sdk.LvLIVE()

    third_uid = "test-py-tob"
    a_id = "test"
    r = live.GetTokenByThirdUID(third_uid, a_id, user_name='test-py',
                                portrait_uri='http://meet.linkv.sg/app/rank-list/static/img/defaultavatar.cd935fdb.png')

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
    unique_id = '123123123'
    gold = 10
    r2 = live.SuccessOrderByLiveOpenID(live_open_id, unique_id, linkv_sdk.OrderTypeAdd, gold, 10, 1,
                                       linkv_sdk.PlatformTypeH5, '')
    if not r2['status']:
        print('live.SuccessOrderByLiveOpenID(%s)' % r2['error'])
        return

    golds1 = r2['golds']
    print('golds1:%d' % golds1)
    if (gold + golds0) != golds1:
        print('(golds0+gold) != golds1')
        return

    unique_id1 = '456456456'
    ok = live.ChangeGoldByLiveOpenID(live_open_id, unique_id1, linkv_sdk.OrderTypeDel, gold, 1, 'test del')
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
