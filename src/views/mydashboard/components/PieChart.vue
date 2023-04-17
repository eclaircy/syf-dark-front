<template>
    <div>
        <!-- <el-card shadow="none"> -->
            <div id="site-pie" class="pie-chart" style="margin-bottom:5px"></div>
        <!-- </el-card> -->
        
        <!-- <el-card shadow="none"> -->
            <div id="ip-pie" class="pie-chart"></div>
        <!-- </el-card> -->
    </div>
</template>


<script>
import { Pie, G2 } from '@antv/g2plot';
export default {
    data() {
        return {
            countGroup:'',
        }
    },
    methods:{
        getPanelGroup(){
            //获取总统计数量
            this.axios({
                url:"api/sites/statistic",
                method:'get'
            }).then(res=>{
                console.log(res);
                this.countGroup=res.data;
                var siteData=[
                    { type: '恶意网站', value: this.countGroup.malSiteCount  },
                    { type: '正常网站', value: this.countGroup.goodSiteCount  },
                ]
                var ipData = [
                    { type: '恶意IP', value: this.countGroup.malIpCount  },
                    { type: '正常IP', value: this.countGroup.goodIpCount  },
                ]
                this.showPie("site-pie",siteData)
                this.showPie("ip-pie",ipData)
            })
        },
        showPie(contanierId,data){
            const colorList = [["#63DAAB","#6395F9"],["",""]];
            const G = G2.getEngine('canvas');
            const cfg = {               
                appendPadding: 10,
                data,
                autoFit:true,
                animate:true,
                angleField: 'value',
                colorField: 'type',
                radius: 0.75,
                legend: false,
                // color:["#f123","#e4222"],
                label: {
                    type: 'spider',
                    labelHeight: 40,
                    formatter: (data, mappingData) => {
                    const group = new G.Group({});
                    group.addShape({
                        type: 'circle',
                        attrs: {
                        x: 0,
                        y: 0,
                        width: 40,
                        height: 50,
                        r: 5,
                        fill: mappingData.color
                        },
                    });
                    group.addShape({
                        type: 'text',
                        attrs: {
                        x: 10,
                        y: 8,
                        text: `${data.type}`,
                        fill: mappingData.color,
                        },
                    });
                    group.addShape({
                        type: 'text',
                        attrs: {
                        x: 0,
                        y: 25,
                        text: `${data.value}个 ${(data.percent * 100).toFixed(2)}%`,
                        fill: 'rgba(0, 0, 0, 0.65)',
                        fontWeight: 700,
                        },
                    });
                    return group;
                    },
                },
                interactions: [{ type: 'element-selected' }, { type: 'element-active' }],
                }
                const piePlot = new Pie(contanierId, cfg);
                piePlot.render();
        }, 
    },
    created(){
        this.getPanelGroup()
    },
}
</script>

<style scoped>
    .pie-chart{
        height:170px;
        border:1px solid #ddd;
        border-radius:10px
    }
</style>