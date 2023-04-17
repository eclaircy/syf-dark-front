<template>
    <div>
        <div id="area-line-container"></div>   
    </div>

</template>

<script>
import { Line } from '@antv/g2plot';

export default {
    methods: {
        async show(){
        //     const res = await this.axios({
        //         url:'api/sites/statistic/year',
        //         method:'get'
        //     })
        // //     .then(res=>{
        //         console.log(res.data);
        //         var data = res.data;

        // })
            fetch('api/sites/statistic/year')
            .then((res) => res.json())
            .then((data) => {
                const linePlot = new Line('area-line-container', {
                    data,
                    height:340,
                    xField: 'year',
                    yField: 'value',
                    seriesField: 'type',
                    // yAxis: {
                    //     label: {
                    //     // formatter: (v) => `${(v / 10e8).toFixed(1)} B`,
                    //     },
                    // },
                    // color: ['#F6BD16 ','#1979C9', '#D62A0D', ],
                    legend: {
                        position: 'top',
                    },
                    // isStack:true,
                    layerOrder: [ '恶意网站', '良性网站','全部IP','全部网站',],
                    smooth: true,
                    // 配置折线趋势填充
                    area: {
                        style: {
                            fillOpacity: 0.15,
                            // opacity:1,startOnZero:false
                        },
                    },
                    // blendMode: 'source-over', // 设置混合模式
                    animation: {
                        appear: {
                        animation: 'wave-in',
                        duration: 1000,
                        },
                    },
                });

                linePlot.render();
            });

        }
    },
    mounted(){
        this.show()
    }
}
</script>