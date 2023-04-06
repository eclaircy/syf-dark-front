<template>
    <div >
        <div v-for="i in 4" style="margin-bottom:10px"> 
            {{ itemList[i-1].type }}
            <div style="height:25px;overflow:hidden"> 
                <div :id="`percent-container-${i}`" ></div>
            </div>
            
        </div>
    </div>
</template>

<script>
import { Progress } from '@antv/g2plot';

export default {
    data(){
        return{
            itemList:[
                {
                    type:"恶意网站",
                    percentage:0.70
                },
                {
                    type:"良性网站",
                    percentage:0.90
                },
                {
                    type:"恶意IP",
                    percentage:0.60
                },
                {
                    type:"良性IP",
                    percentage:0.50
                },
            ]
        }
    },
    methods:{
        showPercentageBar(array){
            const colorList = ["#007BFF","#DC3545","#28A745","#FFC107"];
            for (let index = 0; index < array.length; index++) {
                const element = array[index];
                const progress = new Progress('percent-container-'+(index+1), {
                    height: 40,
                    width: 350,
                    autoFit: false,
                    percent: this.itemList[index].percentage,
                    barWidthRatio: 0.3,
                    color: [colorList[index], '#E8EDF3'],
                });
                progress.render();
                
            }
        }
    },
    mounted(){
        this.showPercentageBar(this.itemList)
    }
}
</script>