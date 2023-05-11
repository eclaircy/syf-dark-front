<template>
    <div>
            <!-- TODO:描述：全部下载网站数量、ip数量、 -->
            <div id="stack-area-container"></div>   
    </div>

</template>

<script>
import { Area } from '@antv/g2plot';

export default {
    data(){
        return{

        }
    },
    methods:{
        //TODO:也可以改成line area：https://g2plot.antv.antgroup.com/zh/examples/line/multiple/#line-area
        showStackArea(){
            //https://gw.alipayobjects.com/os/bmw-prod/b21e7336-0b3e-486c-9070-612ede49284e.json
            this.axios({
                url:'api/sites/statistic/year',
                method:'get'
            }).then(res=>{
                console.log(res.data);
                var data = res.data;
                const area = new Area('stack-area-container', {
                data,
                
                smooth:true,
                autoFit:true,
                xField: 'year', //'date'
                yField: 'value', //'value'
                seriesField: 'type', //'country'
                height:350,
                color:["#945FB9","#F6BD16","#5B8FF9","#5AD8A6"],
                slider: {
                    start: 0.5,
                    end: 1,
                },
                });
                area.render();
            })

        },
        showSampleStackArea(){
            this.axios({
                url:'https://gw.alipayobjects.com/os/bmw-prod/b21e7336-0b3e-486c-9070-612ede49284e.json',
                method:'get'
            }).then(res=>{
                console.log(res.data);
                var data = res.data;
                const area = new Area('stack-area-container', {
                data,
                autoFit:true,
                xField: 'date', //'date'
                yField: 'value', //'date'
                seriesField: 'country', //'country'
                height:350,
                // TODO:配置折线趋势填充 这里是自己加的，不确定能不能兼容
                // area: {
                //     style: {
                //     fillOpacity: 0.15,
                //     },
                // },
                // animation: {
                //     appear: {
                //     animation: 'wave-in',
                //     duration: 3000,
                //     },
                // },
                /////////////////////////////
                slider: {
                    start: 0.1,
                    end: 0.9,
                },
                });
                area.render();
            })

        }
    },
    mounted(){
        this.showStackArea()
        // this.showSampleStackArea()
    }
}
</script>

<style scoped>
    .h4{
        margin: 0px; padding: 0px;
        line-height:1;
    }

</style>