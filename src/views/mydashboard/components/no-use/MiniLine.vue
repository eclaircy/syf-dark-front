<template>
    <div id="mini-container"></div>
</template>

<script>

import { TinyArea } from '@antv/g2plot';
export default {
    methods:{
        showMini(){     
            const data = [
            264,
            417,
            438,
            887,
            309,
            397,
            550,
            575,
            563,
            430,
            525,
            592,
            492,
            467,
            513,
            546,
            983,
            340,
            539,
            243,
            226,
            192,
            ];
            const tinyArea = new TinyArea('mini-container', {
            height: 60,
            autoFit: false,
            data,
            smooth: true,
            });
            tinyArea.render();
        }
    },
    mounted(){
        this.showMini()
    }
}
</script>