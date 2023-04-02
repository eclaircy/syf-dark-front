<template>
    <div>
        <div id="bar" style="height:366px"> </div>
    </div>
</template>

<script>

import echarts from 'echarts';
require('echarts/lib/component/title');
require('echarts/lib/component/toolbox');
require('echarts/lib/component/tooltip');
require('echarts/lib/component/grid');
require('echarts/lib/component/legend');
require('echarts/lib/chart/line');
export default {
    data(){
        return{
            
        }
    },
    methods:{
        showBarChart(){
            var chartDom = document.getElementById('bar');
            var myChart = echarts.init(chartDom);
            var option;

            option = {
            color:['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc'],
            title: {
                text: 'Stacked Area Chart'
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                type: 'cross',
                label: {
                    backgroundColor: '#6a7985'
                }
                }
            },
            legend: {
                data: ['网站总数', '恶意网站数', '恶意IP数', '恶意团伙数', 'Search Engine']
            },
            toolbox: {
                feature: {
                saveAsImage: {}
                }
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: [
                {
                type: 'category',
                boundaryGap: false,
                data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                }
            ],
            yAxis: [
                {
                type: 'value'
                }
            ],
            series: [        
                {
                name: '网站总数',
                type: 'line',

                symbol: 'triangle', //三角形图标
                symbolSize: 14,//三角形大小

                stack: 'Total',
                areaStyle: {},
                emphasis: {
                    focus: 'series'
                },
                data: [120, 132, 101, 134, 90, 230, 210],
                },
                {
                    name: '恶意网站数',
                    type: 'line',
                    stack: 'Total',
                    areaStyle: {},
                    emphasis: {
                        focus: 'series'
                    },
                    data: [220, 182, 191, 234, 290, 330, 310],
                    // markPoint: {
                    //     data: [
                    //     { type: 'max', name: 'Max' },
                    //     { type: 'min', name: 'Min' }
                    //     ]
                    // },
                },
                {
                name: '恶意IP数',
                type: 'line',
                stack: 'Total',
                areaStyle: {},
                emphasis: {
                    focus: 'series'
                },
                data: [150, 232, 201, 154, 190, 330, 410]
                },
                {
                name: '恶意团伙数',
                type: 'line',
                stack: 'Total',
                areaStyle: {},
                emphasis: {
                    focus: 'series'
                },
                data: [320, 332, 301, 334, 390, 330, 320]
                },
                {
                name: 'Search Engine',
                type: 'line',
                stack: 'Total',
                label: {
                    show: true,
                    position: 'top'
                },
                areaStyle: {},
                emphasis: {
                    focus: 'series'
                },
                data: [820, 932, 901, 934, 1290, 1330, 1320]
                }
            ]
            };
            option && myChart.setOption(option);
        }
    },
    mounted(){
        this.showBarChart()
    }
}
</script>