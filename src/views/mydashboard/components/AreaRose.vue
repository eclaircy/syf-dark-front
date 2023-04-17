<template>
    <div id="rose-container" style="height:200px"></div>
</template>

<script>
import { Rose } from '@antv/g2plot';

export default {
    methods: {
        showRose(){
            
            const data = [
            { type: '中国', value: 726 },
            { type: '美国', value: 46 },
            { type: '日本', value: 6 },
            { type: '韩国', value: 5 },
            { type: '新加坡', value: 3 },
            // { type: '其他', value: 5 },
            ];

            const rosePlot = new Rose('rose-container', {
            data,
            // autoFit:true,
            // padding:[16, 8, 16, 8], //上右下左
            xField: 'type',
            yField: 'value',
            seriesField: 'type',
            radius: 0.9,
            color:["#2EC7C9","#C8B2F4","#5AB1EF","#FFB980","#ED868C","#8D98B3"],
            label: {
                offset: -15,
            },
            });

            rosePlot.render();
        }
    },
    mounted() {
        this.showRose()
    },
}
</script>