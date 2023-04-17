const Mock = require('mockjs')

const List = []
const count = 11

const baseContent = '<p>I am testing data, I am testing data.</p><p><img src="https://wpimg.wallstcn.com/4c69009c-0fd4-4153-b112-6cb53d1cf943"></p>'
const image_uri = 'https://wpimg.wallstcn.com/e4558086-631c-425c-9430-56ffb46e70b3'
const titelList = ['https://www.sh-seekers.com/40175.html','http://www.pipikun.com/android/soft/8460.html','https://www.okemu.com/azsoft/520799.html','https://www.okemu.com/azsoft/520799.html','https://m.zhouji365.com/app/11397.html','http://www.xp7.com/soft/jyjx/65385.html','http://www.laoyoutiao.net/yyxz/69.html','http://www.ziku8.cn/ziti/17258.html','https://www.42824.com/html/fangzhengshaoerjianti.html','https://www.pszxw.net/xz/35425.html','http://www.aiskycn.com/az/1217086.html','https://www.youxigt.com/app/88444.html','https://ishare.iask.sina.com.cn/f/aOKADWaCkl.html?ivk_sa=1024320u','http://www.ysysj.net/List/62079/Default.aspx',]


// 生成指定范围内的随机整数
function randomInteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}


for (let i = 0; i < count; i++) {
  List.push(Mock.mock({
    id: i+1,
    timestamp: '2023-4-05-'+" "+randomInteger(20,23)+":"+randomInteger(1,59),  //Mock.Random.date('T'),
    author: '@first',
    reviewer: '@first',
    title: titelList[i],
    content_short: 'mock data',
    content: baseContent,
    forecast: '@float(0, 100, 2, 2)',
    importance: '@integer(1, 3)',
    'type|1': ['CN', 'US', 'JP', 'EU'],
    'status|1': ['doing','done', 'draft'],
    display_time: '@datetime',
    comment_disabled: true,
    pageviews: '@integer(300, 5000)',
    image_uri,
    platforms: ['a-platform']
  }))
}

module.exports = [
  {
    url: '/vue-element-admin/article/list',
    type: 'get',
    response: config => {
      const { importance, title, page = 1, limit = 20, sort,status } = config.query

      let mockList = List.filter(item => {
        if (importance && item.importance !== +importance) return false
        // if (type && item.type !== type) return false
        if (title && item.title.indexOf(title) < 0) return false
        // test
        if (status && item.status!==status) return false
        return true
      })

      if (sort === '-id') {
        mockList = mockList.reverse()
      }

      const pageList = mockList.filter((item, index) => index < limit * page && index >= limit * (page - 1))

      return {
        code: 20000,
        data: {
          total: mockList.length,
          items: pageList
        }
      }
    }
  },

  {
    url: '/vue-element-admin/article/detail',
    type: 'get',
    response: config => {
      const { id } = config.query
      for (const article of List) {
        if (article.id === +id) {
          return {
            code: 20000,
            data: article
          }
        }
      }
    }
  },

  {
    url: '/vue-element-admin/article/pv',
    type: 'get',
    response: _ => {
      return {
        code: 20000,
        data: {
          pvData: [
            { key: 'PC', pv: 1024 },
            { key: 'mobile', pv: 1024 },
            { key: 'ios', pv: 1024 },
            { key: 'android', pv: 1024 }
          ]
        }
      }
    }
  },

  {
    url: '/vue-element-admin/article/create',
    type: 'post',
    response: _ => {
      return {
        code: 20000,
        data: 'success'
      }
    }
  },

  {
    url: '/vue-element-admin/article/update',
    type: 'post',
    response: _ => {
      return {
        code: 20000,
        data: 'success'
      }
    }
  }
]

