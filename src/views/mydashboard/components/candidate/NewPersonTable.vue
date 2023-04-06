<template>
    <div>
        <el-scrollbar  style="height: 100%;" class="scrollbar-for">
            <el-card v-for="i in 7" shadow="hover" class="new-person-card">
            <el-avatar shape="circle" size="medium" src="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"></el-avatar>
            蔡远卓
            </el-card>
        </el-scrollbar>

    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
    .new-person-card{
        border-radius: 10px;
        height: 64px;
        margin-bottom: 5px;
    }

    .new-person-card.hover{
        background-color: #f8f9fa;
    }
</style>