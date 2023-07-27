<template>
    <div>
        <!-- 管理系统爬虫：起始时间、结束时间 -->
        <el-card class="timeline-card">
            <span>团伙时间轴</span>
            <el-scrollbar style="height:510px;" wrap-style="overflow-x:hidden;">
            <div class="timeline-container">
                <a-timeline mode="alternate" style="margin-top:5px;" >
                    <a-timeline-item v-for="(item,index) in nodes" :color="timeling_color[item.label]" :key="index">
                        团伙{{item.cluster_id}}: 新增{{ nodeType[item.label] }}{{ item.properties.name }}  
                        <div>{{ item.properties.start_time}}</div>
                    </a-timeline-item>
                </a-timeline>
            </div>
            </el-scrollbar>
        </el-card>
    </div>
</template>

<script>
let pinyin = require('js-pinyin');
pinyin.setOptions({checkPolyphone: false, charCase: 0});

export default {
    data(){
        return{
            nodes:'',
            timeling_color :{"website:":"green","company":"red","person":"blue"},
            nodeType:{"website:":"网站","company":"公司","person":"人员"},
        }
    },
    methods:{
        showTimeLine(){
             //拿到各种类型的node之后，遍历所有的节点：
            // 把website按照start_time放进去；company的register_time放进去；
            // 当node是person类型，查询edges数组中它和company的边，把company的register_time放进去；
            const timeling_color = {"website:":"green","company":"red","person":"blue"};

            this.nodes = [
                {"id": 1,cluster_id:"c1",label:"website", "properties":{"start_time": "2020-3-23","name":"www"}},
                {"id": 2,cluster_id:"c2",label:"company",   "properties":{"start_time": "2021-2-15","name":"www"}},
                {"id": 3,cluster_id:"c3",label:"person",   "properties":{"start_time": "2019-9-8","name":"www"}}
            ];

            nodes.sort(function(a, b) {
                var dateA = new Date(a.start_time);
                var dateB = new Date(b.start_time);
                return dateB - dateA; // 按照日期从最新到最旧进行排序
            });
            console.log(nodes);
        },
        showPinyin(){
            console.log(pinyin.getFullChars('徐').toUpperCase());
            console.log(pinyin.getFullChars('管理员'));
            console.log(pinyin.getCamelChars('管理员'));

        }
    },
    mounted(){
    //    this.showTimeLine();
       this.showPinyin();
    }

}
</script>
<style scoped>
.timeline-card{
    height:566px;
}

.ant-timeline-item{
    color: #fff !important;
  }

</style>