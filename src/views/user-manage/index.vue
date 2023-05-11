<template>
    <!-- 此页面管理员可见，管理用户：管理员/普通用户/执法监管人员 -->
    <div style="padding:20px;height:700px;">
        <el-row style="margin-bottom:20px;">
            <el-card>
                 <div style="font-size: 20px;margin-bottom: 7px;">系统用户管理</div>
                 <span>管理员、执法人员、普通用户</span>
                 <!-- <el-divider></el-divider> -->
            </el-card>
        </el-row>
        
        <el-card style="padding:30px;">
                <el-button @click="handleCreate">新增用户</el-button>
                <el-table :data="users" style="width: 100%">
                    <el-table-column label="序号" width="180"  type="index">
                    </el-table-column>
        
                    <el-table-column label="用户名" width="180">
                    <template slot-scope="scope">
                        {{ scope.row.username }}
                    </template>
                    </el-table-column>
        
                    <el-table-column label="邮箱" >
                        <template slot-scope="scope">
                            <span style="margin-left: 10px">{{ scope.row.email }}</span>
                        </template>
                    </el-table-column>
        
                    <el-table-column label="用户权限" >
                        <template slot-scope="scope">
                            <div slot="reference" class="name-wrapper">
                                <el-tag size="medium" color="danger">{{ role[scope.row.roleId] }}</el-tag>
                            </div>
                        </template>
                    </el-table-column>
            
                    <el-table-column label="操作">
                    <template slot-scope="scope">
                        <el-button size="mini"  @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                        <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                    </template>
                    </el-table-column>
                </el-table>
        </el-card>

        <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
            <el-form ref="dataForm" :rules="rules" :model="temp"  label-position="left" label-width="90px" style="width: 400px; margin-left:50px;">
              <el-form-item label="用户名" prop="username">
                <el-input v-model="temp.username" />
              </el-form-item>
    
              <el-form-item label="密码" prop="password" v-if="dialogStatus=='create'">
                <el-input type="password" v-model="temp.password" autocomplete="off"></el-input>
              </el-form-item>

              <el-form-item label="确认密码" prop="checkPass" v-if="dialogStatus=='create'">
                <el-input type="password" v-model="temp.checkPass" autocomplete="off"></el-input>
              </el-form-item>

              <el-form-item label="邮箱" prop="email">
                <el-input v-model="temp.email"  />
              </el-form-item>

              <el-form-item label="用户权限" prop="role">
                <el-select v-model="temp.selectValue" placeholder="请选择">
                    <el-option label="普通用户" value="1"></el-option>
                    <el-option label="执法人员" value="2"></el-option>
                    <el-option label="管理员" value="3"></el-option>
                    <!-- <el-option v-for="item in temp.selectOptions" :key="item.value" :label="item.label"  :value="item.value"></el-option> -->
                  </el-select>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogFormVisible = false"> 取消 </el-button>
              <el-button @click="resetForm('dataForm')"  v-if="dialogStatus=='create'">重置</el-button>
              <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
                <span v-if="dialogStatus=='create'">创建</span>
                <span v-if="dialogStatus=='update'">更新</span>
              </el-button>
            </div>
        </el-dialog>
    </div>

</template>
  
<script>
export default {
    data() {
        var validatePass = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请输入密码'));
            } else {
                if (this.temp.checkPass !== '') {
                    this.$refs.dataForm.validateField('checkPass');
                }
                callback();
            }
        };
        var validatePass2 = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请再次输入密码'));
            } else if (value !== this.temp.password) {
                callback(new Error('两次输入密码不一致!'));
            } else {
                callback();
            }
        };
        return {
            users:[],
            role:{
                1:"管理员",
                2:"执法人员",
                3:"普通用户",
            },
            dialogFormVisible:false,
            dialogStatus: '',
            textMap: {
                update: '编辑',
                create: '创建'
            },
            rules: {
                username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
                password: [ {required: true, validator: validatePass, trigger: 'blur' },{ min: 6, max: 10, message: '密码长度在 6 到 10 个字符', trigger: 'blur' } ],
                checkPass: [{required: true, validator: validatePass2, trigger: 'blur' } ],
                email: [{ required: true, message: '请输入邮箱地址', trigger: 'blur' },
                        { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }],
                selectValue: [{ required: true, message: '请选择用户角色', trigger: 'blur' } ],
            },
            temp: {
                id: undefined,
                username:'',
                password:'',
                checkPass:'',
                email:'',
                selectValue: '1',
            },
        }
    },
    watch:{
        dialogFormVisible(newVal,oldVal){
            if(newVal==false){
                console.log("关闭表单")
                this.resetForm("dataForm")
                // this.dialogStatus = ''
                console.log(this.temp)
            }
        },
        temp(newVal,oldVal){
            console.log(newVal)
        }
        },
    methods: {
        handleEdit(index, row) {
            console.log(index, row);
            this.temp = Object.assign({}, row) // copy obj
            this.temp.selectValue=this.role[row.roleId]
            this.dialogStatus = 'update'
            this.dialogFormVisible = true
            this.$nextTick(() => {
                this.$refs['dataForm'].clearValidate()
            })
        },
        handleDelete(index, row) {
            console.log(index, row);
        },
        handleCreate() {
            this.dialogStatus = 'create'
            this.dialogFormVisible = true
            // this.$nextTick(() => {
            //     this.resetForm("dataForm")
            //     this.$refs['dataForm'].clearValidate()
            // })
        },
        resetForm(formName) {
            this.dialogStatus = ''
            this.temp={
                id: undefined,
                username:'',
                password:'',
                checkPass:'',
                email:'',
                selectValue: '1',
            }
            this.$refs[formName].resetFields();
            console.log("reset:",this.temp)
            // this.$refs[formName].clearValidate()
        },
        createData() {
            this.$refs['dataForm'].validate((valid) => {
            if (valid) {
                // mysql
                this.dialogFormVisible = false
                this.$notify({
                    title: 'Success',
                    message: '增加用户成功',
                    type: 'success',
                    duration: 2000
                })
                // this.temp.id = parseInt(Math.random() * 100) + 1024 // mock a id
                // createArticle(this.temp).then(() => {
                //     this.list.unshift(this.temp)
                //     this.dialogFormVisible = false
                //     this.$notify({
                //         title: 'Success',
                //         message: '增加用户成功',
                //         type: 'success',
                //         duration: 2000
                //     })
                // })
            }
            })
        },
        updateData(){
            this.$refs['dataForm'].validate((valid) => {
            if (valid) {
                // mysql
                this.dialogFormVisible = false
                this.$notify({
                    title: 'Success',
                    message: '更新用户资料成功',
                    type: 'success',
                    duration: 2000
                })
            }
            })
        },
        getAllUser(){
            this.axios({
                url: "api/user/all",
                method:'get',
            }).then(res=>{
                this.users=res.data;
                console.log(res.data)
            })
        },
        
    },
    mounted(){
        this.getAllUser()
    }
}
</script>

<style scoped>
    /deep/.el-table th.el-table__cell.is-leaf, .el-table td.el-table__cell {
        border-left: transparent !important; 
        border-top: transparent !important;
    }
    /deep/.el-input__inner {
        background-color: #222933;
        border: 1px solid #eee;
        color: #eee;
    }
</style>