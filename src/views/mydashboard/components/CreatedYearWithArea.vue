<template>
    <div id="area" :style="{height:height,width:width,background:background}"></div>
</template>


<script>
import echarts from 'echarts';
import resize from '../../dashboard/admin/components/mixins/resize'
require('echarts/lib/component/dataset');
require('echarts/lib/component/tooltip');
require('echarts/lib/component/grid');
require('echarts/lib/component/legend');
require('echarts/lib/chart/line');
require('echarts/lib/chart/pie');

export default {
    mixins: [resize],
    props: {
        width: {
            type: String,
            default: '100%'
        },
        height: {
            type: String,
            default: '360px'
        },
        autoResize: {
            type: Boolean,
            default: true
        },
        background:{
            type: String,
            default: "#fff"
        }
    },
    data() {
        return {
            chart: null
        }
    },
    methods:{
        showAreaSitesCreatedYearLineChart(){
            var chartDom = document.getElementById('area');
            var myChart = echarts.init(chartDom);
            var option;
            setTimeout(function () {
            option = {
                legend: {},
                tooltip: {
                trigger: 'axis',
                showContent: false
                },
                dataset: {
                source: [
                    ['江苏', '2012', '2013', '2014', '2015', '2016', '2017'],
                    ['武汉', 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
                    ['湖南', 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
                    ['香港', 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
                    ['上海', 25.2, 37.1, 41.2, 18, 33.9, 49.1],
                    ['澳门', 30.1, 23, 45, 67, 56,78]
                ]
                },
                xAxis: { type: 'category' },
                yAxis: { gridIndex: 0 },
                grid: { top: '55%' },
                color: ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc'],
                series: [
                {
                    type: 'line',
                    smooth: true,
                    seriesLayoutBy: 'row',
                    emphasis: { focus: 'series' }
                },
                {
                    type: 'line',
                    smooth: true,
                    seriesLayoutBy: 'row',
                    emphasis: { focus: 'series' }
                },
                {
                    type: 'line',
                    smooth: true,
                    seriesLayoutBy: 'row',
                    emphasis: { focus: 'series' }
                },
                {
                    type: 'line',
                    smooth: true,
                    seriesLayoutBy: 'row',
                    emphasis: { focus: 'series' }
                },
                {
                    type: 'pie',
                    id: 'pie',
                    radius: '30%',
                    center: ['50%', '25%'],
                    emphasis: {
                    focus: 'self'
                    },
                    label: {
                    formatter: '{b}: {@2012} ({d}%)'
                    },
                    encode: {
                    itemName: 'product',
                    value: '2012',
                    tooltip: '2012'
                    }
                }
                ]
            };
            myChart.on('updateAxisPointer', function (event) {
                const xAxisInfo = event.axesInfo[0];
                if (xAxisInfo) {
                const dimension = xAxisInfo.value + 1;
                myChart.setOption({
                    series: {
                    id: 'pie',
                    label: {
                        formatter: '{b}: {@[' + dimension + ']} ({d}%)'
                    },
                    encode: {
                        value: dimension,
                        tooltip: dimension
                    }
                    }
                });
                }
            });
            myChart.setOption(option);
            });
            option && myChart.setOption(option);
        },
    },
    mounted(){
        this.showAreaSitesCreatedYearLineChart();
    }
}
</script>

<style scoped>

</style>