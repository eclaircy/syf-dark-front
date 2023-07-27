<template>
    <div id="area-bar" style="height:375px"></div>
</template>
<!-- 170px -->
<script>
import { Column } from '@antv/g2plot';
export default {
    methods:{
        getAreaInfo(){
            this.axios({
                url:"api/sites/statistic/area",
                method:'get'
            }).then(res=>{
                console.log(res.data);
                this.showAreaBar(res.data);
            });
        },
        showAreaBar(data){
            const stackedColumnPlot = new Column('area-bar', {
                data,
                // height:200,
                autoFit:true,
                isStack: true,
                xField: 'area',
                yField: 'value',
                seriesField: 'type',
                //TODO:设置文字倾斜
                xAxis: {
                    label: {
                    autoHide: true,
                    autoRotate: true,
                    size:12
                    // rotate:30,
                    },
                },
                // label: {
                //     // 可手动配置 label 数据标签位置
                //     position: 'middle', // 'top', 'bottom', 'middle'
                //     layout: [{ type: 'interval-hide-overlap' }], // 隐藏重叠文字
                // },

                legend: {
                    position:'top',
                    itemName: {
                        style: (item, index) => {
                            return {
                            fill:  '#C2C2C2',
                            };
                        },
                    },
                },
                interactions: [{ type: 'active-region', enable: false }],
                connectedArea: {
                    style: (oldStyle, element) => {
                    return { fill: 'rgba(0,0,0,0.25)', stroke: oldStyle.fill, lineWidth: 0.5 };
                    },
                },
                slider: {
                    start: 0,
                    end: 0.9,
                },
            });

            stackedColumnPlot.render();
        }
    },
    mounted(){
        this.getAreaInfo()
    }
}
</script>