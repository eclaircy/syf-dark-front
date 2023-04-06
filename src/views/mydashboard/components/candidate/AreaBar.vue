<template>
    <div id="area-bar" style="height:200px"></div>
</template>

<script>
import { Column } from '@antv/g2plot';
export default {
    methods:{
        showAreaBar(){
            var typeList = ["恶意","良性"]
            var data = [
                {
                    "year": "武汉",
                    "value": 3,
                    "type": "Lon"
                },
                {
                    "year": "上海",
                    "value": 4,
                    "type": "Lon"
                },
                {
                    "year": "1993",
                    "value": 3.5,
                    "type": "Lon"
                },
                {
                    "year": "1994",
                    "value": 5,
                    "type": "Lon"
                },
                {
                    "year": "1995",
                    "value": 4.9,
                    "type": "Lon"
                },
                {
                    "year": "1996",
                    "value": 6,
                    "type": "Lon"
                },
                {
                    "year": "1997",
                    "value": 7,
                    "type": "Lon"
                },
                {
                    "year": "1998",
                    "value": 9,
                    "type": "Lon"
                },
                {
                    "year": "1999",
                    "value": 13,
                    "type": "Lon"
                },
                {
                    "year": "武汉",
                    "value": 3,
                    "type": "Bor"
                },
                {
                    "year": "上海",
                    "value": 4,
                    "type": "Bor"
                },
                {
                    "year": "1993",
                    "value": 3.5,
                    "type": "Bor"
                },
                {
                    "year": "1994",
                    "value": 5,
                    "type": "Bor"
                },
                {
                    "year": "1995",
                    "value": 4.9,
                    "type": "Bor"
                },
                {
                    "year": "1996",
                    "value": 6,
                    "type": "Bor"
                },
                {
                    "year": "1997",
                    "value": 7,
                    "type": "Bor"
                },
                {
                    "year": "1998",
                    "value": 9,
                    "type": "Bor"
                },
                {
                    "year": "1999",
                    "value": 13,
                    "type": "Bor"
                }
                ];
            // fetch('https://gw.alipayobjects.com/os/antfincdn/8elHX%26irfq/stack-column-data.json')
            // .then((data) => data.json())
            // .then((data) => {
                const stackedColumnPlot = new Column('area-bar', {
                data,
                // height:200,
                autoFit:true,
                isStack: true,
                xField: 'year',
                yField: 'value',
                seriesField: 'type',
                label: {
                    // 可手动配置 label 数据标签位置
                    position: 'middle', // 'top', 'bottom', 'middle'
                },
                interactions: [{ type: 'active-region', enable: false }],
                connectedArea: {
                    style: (oldStyle, element) => {
                    return { fill: 'rgba(0,0,0,0.25)', stroke: oldStyle.fill, lineWidth: 0.5 };
                    },
                },
                });

                stackedColumnPlot.render();
            // });

        }
    },
    mounted(){
        this.showAreaBar()
    }
}
</script>