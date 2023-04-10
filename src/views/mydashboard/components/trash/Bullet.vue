<template>
    <div>
        <div id="bullet-container"></div>
        <div v-for="i in 4" :id="`bullet-container-${i}`">
            s
        </div>
    
    </div>

</template>

<script>
import { Bullet } from '@antv/g2plot';
export default {
    data(){
        return{
            bulletData:[
                {
                    title: '恶意网站',
                    ranges: [100],
                    measures: [80],
                    target: 0,
                },
                {
                    title: '恶意网站',
                    ranges: [100],
                    measures: [80],
                    target: 0,
                },
            ],
        }
    },
    methods:{
        showBullet(bulletData){
            // @TODO 差一张垂直方向的缩略图
            const colorList = [];
            for (let index = 0; index < bulletData.length; index++) {
                const element = bulletData[index];
                var containerId = "bullet-container-";
                console.log(containerId.concat(index+1));
                const bulletPlot = new Bullet(containerId.concat(index+1), {
                    element,
                    measureField: 'measures',
                    rangeField: 'ranges',
                    targetField: 'target',
                    xField: 'title',
                    color: {
                        range: '#f0efff',
                        measure: '#007BFF',
                        target: '#007BFF',
                    },
                    xAxis: {
                        line: null,
                    },
                    yAxis: false,
                    layout: 'horizontal',
                    label: {
                        measure: {
                        position: 'middle',
                        style: {
                            fill: '#fff',
                        },
                        },
                    },
                });
                bulletPlot.render();
            }
        }
    },
    mounted(){
        this.showBullet(this.bulletData)
    }
    
}
</script>