<template>
    <!-- 此页面管理员可见，管理用户：管理员/普通用户/执法监管人员 -->
    <div style="padding:20px;">
        <el-row style="margin-bottom:20px;">
            <el-card>
                 <div style="font-size: 20px;margin-bottom: 7px;">系统用户管理</div>
                 <span>管理员、执法人员、普通用户账号管理</span>
                 <!-- <el-divider></el-divider> -->
            </el-card>
        </el-row>
        
        <el-card style="padding:30px;margin-bottom:15px;">
                <el-button @click="handleCreate">新增用户</el-button>
                <el-table :data="users" style="width: 100%">
                    <el-table-column label="id" width="180" >
                        <template slot-scope="scope">
                            {{ scope.row.id }}
                        </template>
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
                                <!-- <svg t="1686317740921" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5243" width="32" height="32"><path d="M768.579 668.846c-24.876-24.876-89.719-40.348-129.598-47.739a514.907 514.907 0 0 1 5.813 5.75l24.641 76.001-26.866 25.721 21.074 45.864L630.396 963.5h71.906l3.228-98.451 5.66 98.451h93.671c-1.752-77-8.758-267.126-36.282-294.654zM380.624 728.565l-26.871-25.74 24.642-76.031s2.229-2.231 5.864-5.677c-39.935 7.453-104.112 23.014-128.833 47.729C227.902 696.374 220.892 886.5 219.14 963.5h90.283l5.658-98.451 3.227 98.451h74.485l-33.24-189.067 21.071-45.868z" fill="#8198C8" p-id="5244"></path><path d="M437.608 588.48a362.253 362.253 0 0 1 1.6-5.242 178.502 178.502 0 0 0-1.6 5.242z" fill="#FFCFBA" p-id="5245"></path><path d="M481.77 626.794l30.229 55.313 29.421-55.313s26.08-13.438 38.08-33.745v-42.492c-12 21.974-34.099 34.123-74.371 34.123-38.519 0-55.629-11.316-72.629-31.865v28.286c9-0.378 4.349-0.796 5.205-1.099 2.338 26.905 44.065 46.792 44.065 46.792z" fill="#FFCFBA" p-id="5246"></path><path d="M505.129 584.68c40.272 0 62.371-12.149 74.371-34.123v-4.04c-16 18.99-34.318 29.395-71.615 29.395-40.295 0-52.385-12.383-75.385-34.783v11.687c17 20.547 34.111 31.864 72.629 31.864z" fill="#F4B4A7" p-id="5247"></path><path d="M309.423 963.5h8.885l-3.227-98.451zM702.302 963.5h8.888l-5.66-98.451z" fill="#78829A" p-id="5248"></path><path d="M596.029 645.745l-24.776 43.63s-4.677-55.563-28.66-62.581L512 682.107l-30.229-55.313c-23.979 7.018-28.662 62.581-28.662 62.581l-25.039-44.102c-1.509 20.367-1.723 44.086-0.697 71.845 1.053 28.273 24.009 136.382 49.057 246.382h75.119c22.529-110 43.223-218.108 44.271-246.382 1.021-27.704 1.235-51.219 0.209-71.373z" fill="#FFFFFF" p-id="5249"></path><path d="M428.07 645.273l-1.86-3.278c1.629-18.759 7.804-41.465 11.398-53.515 0.51-1.771 1.046-3.52 1.6-5.242 0.645-2.052 1.04-3.236 1.04-3.236-0.854 0.303-1.771 0.721-2.665 1.099-17.713 7.489-42.235 29.521-53.323 40.017-3.635 3.445-5.864 5.677-5.864 5.677l-24.642 76.031 26.871 25.74-21.07 45.867 33.24 189.067h83.636c-25.047-110-48.003-218.108-49.057-246.382-1.027-27.759-0.813-51.477 0.696-71.845z" fill="#848FC1" p-id="5250"></path><path d="M585.144 580.845c0.104 0.305 0.194 0.623 0.296 0.927 0.028-0.253 0.108-0.494 0.134-0.754-0.143-0.049-0.294-0.126-0.43-0.173z" fill="#3B433F" p-id="5251"></path><path d="M642.569 728.565l26.866-25.74-24.641-76.031s-2.193-2.28-5.813-5.818c-11.088-10.822-35.748-33.548-53.396-39.949 0.103 0.343 10.248 34.202 12.571 60.969l-2.128 3.75c1.026 20.154 0.813 43.669-0.209 71.373-1.048 28.273-21.741 136.382-44.271 246.382H630.395l33.247-189.067-21.073-45.869z" fill="#848FC1" p-id="5252"></path><path d="M440.247 580.002s-0.396 1.185-1.04 3.236a379.586 379.586 0 0 0-1.6 5.242c-3.594 12.05-9.769 34.756-11.398 53.515l1.86 3.278 25.039 44.102s4.682-55.563 28.662-62.581c0 0-39.185-19.887-41.523-46.792zM542.592 626.794c23.983 7.018 28.66 62.581 28.66 62.581l24.776-43.63 2.128-3.75c-2.323-26.767-12.506-60.626-12.607-60.969 0-0.005-0.049-0.03-0.049-0.03v0.021c0 0.26-0.07 0.501-0.098 0.754-0.451 3.955-1.73 7.713-3.572 11.277-10.488 20.307-39.238 33.746-39.238 33.746z" fill="#BFBFBF" p-id="5253"></path><path d="M511.6 575.911c37.295 0 55.62-10.404 70.247-29.395 10.15-13.174 18.518-30.48 30.201-51.321 7.764-13.84 13.727-29.525 18.264-45.721 3.296 0.817 6.903-0.022 10.726-3.405 11.923-10.523 24.927-61.414 16.149-71.934-2.957-3.569-6.123-4.31-9.008-3.747a330.635 330.635 0 0 1-1.919 12.674c-0.245 1.45-0.54 2.916-0.809 4.377a340.172 340.172 0 0 1-1.644 8.484c-0.122 0.612-0.217 1.207-0.348 1.814-0.011-0.034-0.019 0.772-0.027 0.741-1.423 6.677-3.001 17.021-4.814 21.021h-3.681c2.128-18 3.587-48.408-1.412-71.728-8.662-40.358-38.055-74.985-60.272-71.483-21.917 3.468-39.29 13.543-61.67 13.806-22.385-0.263-39.759-10.651-61.681-14.123-22.213-3.501-51.607 31.493-60.266 71.854-5.005 23.32-3.542 53.675-1.418 71.675h-3.677c-2.61-9-4.771-20.212-6.556-29.714-0.005 0.021-0.009-0.375-0.013-0.358-0.171-0.882-0.306-1.967-0.467-2.854a421.652 421.652 0 0 1-1.018-5.9 300.783 300.783 0 0 1-1.511-10.235c-2.883-0.563-6.043 0.154-9.008 3.725-8.777 10.519 4.231 61.394 16.149 71.917 3.827 3.382 7.444 4.216 10.735 3.396 4.545 16.202 10.514 31.883 18.277 45.725 10.159 18.115 17.887 33.547 26.452 45.926 15.494 22.4 33.726 34.783 74.019 34.783z" fill="#FFCFBA" p-id="5254"></path><path d="M377.505 386.369c0.157 0.858 0.318 2.555 0.48 3.417 1.785 9.502 3.945 20.714 6.556 29.714h3.677c-2.124-18-3.587-48.408 1.418-71.728 8.659-40.358 38.053-74.985 60.266-71.483 21.922 3.468 39.296 13.543 61.681 13.806 22.38-0.263 39.753-10.651 61.67-14.123 22.218-3.501 51.61 31.493 60.272 71.854 4.999 23.32 3.54 53.675 1.412 71.675h3.681c1.813-4 3.392-14.343 4.814-21.021 0.121-0.568 0.256-1.566 0.375-2.14 0.596-2.833 1.127-5.873 1.644-8.694 0.269-1.459 0.563-3.028 0.809-4.479a332.927 332.927 0 0 0 1.919-12.727c5.158-39.742 2.115-76.155-11.381-105.065-21.152-45.317-81.427-64.666-125.215-64.924-43.803 0.258-104.073 19.59-125.226 64.902-13.496 28.915-16.539 65.296-11.381 105.042 0.436 3.368 0.957 6.765 1.511 10.176 0.315 1.923 0.673 3.858 1.018 5.798z" fill="#323232" p-id="5255"></path><path d="M680.683 304.681c0 46.189-0.479 124.096-165.227 124.096-164.771 0-165.214-77.907-165.214-124.096 0-46.15 74.015-56.628 165.214-56.628 91.242 0 165.227 10.478 165.227 56.628z" fill="#686F79" p-id="5256"></path><path d="M515.456 423.365c-158.762 0-164.959-72.299-165.214-118.888v0.207c0 46.188 0.442 124.096 165.214 124.096 164.747 0 165.227-77.907 165.227-124.096v-0.207c-0.286 46.587-6.483 118.888-165.227 118.888z" fill="#686F79" p-id="5257"></path><path d="M753.058 199.494c0 46.914-106.915 84.964-238.769 84.964-131.776 0-238.661-38.05-238.661-84.964 0-46.929 144.74-138.908 238.661-138.908 93.995 0 238.769 91.978 238.769 138.908z" fill="#AAB1BD" p-id="5258"></path><path d="M514.289 87.451c65.482 0 163.265 55.935 179.727 91.711 1.583-3.291 2.434-6.658 2.434-10.087 0-34.226-110.455-101.299-182.16-101.299-71.638 0-182.056 67.073-182.056 101.299 0 3.429 0.852 6.795 2.399 10.087 16.463-35.776 114.214-91.711 179.656-91.711z" fill="#AAB1BD" p-id="5259"></path><path d="M638.335 95.664c39.82 23.673 70.124 52.461 70.124 71.838 0 38.143-86.909 69.079-194.17 69.079-107.194 0-194.067-30.937-194.067-69.079 0-19.378 30.276-48.166 70.125-71.838-62.25 31.007-114.718 75.591-114.718 103.83 0 46.914 106.887 84.964 238.661 84.964 131.854 0 238.769-38.05 238.769-84.964-0.001-28.239-52.466-72.824-114.724-103.83z" fill="#686F79" p-id="5260"></path><path d="M692.565 254.767v-0.095c-0.032-0.079-0.063-0.17-0.095-0.253 0-0.026-0.066-0.06-0.066-0.06-6.003-14.319-82.895-25.649-176.949-25.649-94.011 0-170.962 11.33-176.937 25.649 0 0-0.025 0.033-0.025 0.06-0.038 0.083-0.1 0.173-0.127 0.253 0 0.022-0.031 0.064-0.031 0.095-4.14 9.168-4.266 42.238-0.224 50.95 0.028 0.088 0.16 0.17 0.224 0.278 4.359 14.535 82.009 26.104 177.122 26.104 95.13 0 172.743-11.57 177.142-26.104 0.059-0.109 0.161-0.19 0.194-0.278 4.036-8.713 3.969-41.782-0.228-50.95z" fill="#444B54" p-id="5261"></path><path d="M695.753 281.124c-0.067-2.178-0.123-4.323-0.256-6.43h0.036c-0.036-0.384-0.098-0.729-0.128-1.125 0-0.284-0.03-0.583-0.059-0.883v0.015c-0.163-2.136-0.346-4.186-0.603-6.062-10.687 2.556-24.113 5.023-40.009 7.17-0.256-5.04-4.396-9.065-9.479-9.065-5.247 0-9.519 4.26-9.519 9.507v1.845c-32.302 3.484-72.713 5.773-120.282 5.773-47.554 0-87.941-2.29-120.237-5.773v-1.845c0-5.249-4.301-9.507-9.548-9.507-5.12 0-9.228 4.026-9.48 9.065-15.931-2.146-29.324-4.614-40.037-7.17a133.814 133.814 0 0 0-0.602 6.062v-0.015c-0.035 0.3-0.035 0.6-0.066 0.883-0.029 0.396-0.07 0.741-0.07 1.125-0.12 2.104-0.183 4.251-0.248 6.43 11.598 3.997 25.442 7.774 41.019 11.14 0.129 5.114 4.326 9.229 9.48 9.229 3.86 0 7.201-2.334 8.666-5.655 35.514 6.395 77.674 10.585 121.122 10.585 43.432 0 85.625-4.188 121.132-10.585 1.459 3.322 4.812 5.655 8.669 5.655 5.176 0 9.287-4.115 9.508-9.229 15.555-3.366 29.43-7.143 40.991-11.14z m-40.985 2.889v-2.041a566.326 566.326 0 0 0 21.483-3.3c-6.561 1.836-13.739 3.623-21.483 5.341z m-278.606-2.039v2.041c-7.716-1.719-14.951-3.504-21.525-5.34a591.255 591.255 0 0 0 21.525 3.299z m19.057 5.893v-3.647c36.179 3.814 78.552 5.753 120.237 5.753 41.654 0 84.071-1.94 120.283-5.753v3.647c-33.207 6.09-74.131 10.479-120.283 10.479-46.133 0-87.058-4.389-120.237-10.479z" fill="#444B54" p-id="5262"></path><path d="M338.334 268.249c0-0.038 0.031-0.07 0.031-0.075 0.027-0.083 0.089-0.192 0.127-0.278 0-0.009 0.025-0.027 0.025-0.058 5.975-14.313 82.925-25.626 176.937-25.626 94.053 0 170.944 11.313 176.949 25.626 0 0.029 0.066 0.049 0.066 0.058 0.032 0.085 0.063 0.195 0.095 0.278v0.075c1.705 3.677 2.688 11.283 3.063 19.575 0.571-12.548-0.474-27.395-3.063-33.057v-0.095c-0.032-0.079-0.063-0.17-0.095-0.253 0-0.026-0.066-0.06-0.066-0.06-6.003-14.319-82.895-25.649-176.949-25.649-94.011 0-170.962 11.33-176.937 25.649 0 0-0.025 0.033-0.025 0.06-0.038 0.083-0.1 0.173-0.127 0.253 0 0.022-0.031 0.064-0.031 0.095-2.56 5.661-3.571 20.509-3.035 33.057 0.346-8.295 1.389-15.901 3.035-19.575z" fill="#444B54" p-id="5263"></path><path d="M692.792 292.234c-0.033 0.078-0.136 0.174-0.194 0.267-4.398 14.54-82.012 26.131-177.142 26.131-95.113 0-172.763-11.591-177.122-26.131-0.064-0.092-0.194-0.188-0.222-0.267-1.551-3.317-2.499-10.178-2.813-17.875-0.507 12.283 0.41 26.138 2.813 31.357 0.025 0.088 0.158 0.17 0.222 0.278 4.359 14.535 82.009 26.104 177.122 26.104 95.13 0 172.743-11.57 177.142-26.104 0.059-0.109 0.161-0.19 0.194-0.278 2.394-5.219 3.374-19.074 2.838-31.357-0.349 7.697-1.301 14.558-2.838 17.875z" fill="#444B54" p-id="5264"></path><path d="M695.753 278.436c-0.067-2.887-0.153-5.735-0.406-8.45-35.363 12.496-99.875 25.643-179.891 25.643s-144.515-13.147-179.904-25.643a174.5 174.5 0 0 0-0.381 8.45c40.419 13.924 108.651 25.286 180.285 25.286 71.617 0 139.911-11.363 180.297-25.286z" fill="#F5BF33" p-id="5265"></path><path d="M695.533 271.993c-0.216-2.863-0.443-5.578-0.789-8.059-34.071 8.164-95.593 15.25-179.288 15.25-83.678 0-145.266-7.086-179.302-15.25-0.284 2.481-0.602 5.195-0.736 8.059 41.627 10.083 111.852 15.278 180.038 15.278 68.177 0 138.43-5.195 180.077-15.278z" fill="#F5BF33" p-id="5266"></path><path d="M395.219 289.279c0 5.261-4.301 9.511-9.548 9.511a9.488 9.488 0 0 1-9.507-9.511v-17.725a9.497 9.497 0 0 1 9.507-9.504c5.248 0 9.548 4.268 9.548 9.504v17.725zM635.74 289.279c0 5.261 4.271 9.511 9.518 9.511a9.506 9.506 0 0 0 9.509-9.511v-17.725c0-5.236-4.263-9.504-9.509-9.504-5.247 0-9.518 4.268-9.518 9.504v17.725z" fill="#F5BF33" p-id="5267"></path><path d="M577.339 156.689c0 34.792-28.215 63-63.049 63-34.759 0-62.977-28.208-62.977-63 0-34.79 28.218-63.016 62.977-63.016 34.834 0 63.049 28.225 63.049 63.016z" fill="#444B54" p-id="5268"></path><path d="M515.477 137.086l6.367 12.902 14.236 2.069-10.299 10.04 2.429 14.179-12.733-6.694-12.735 6.694 2.435-14.179-10.303-10.04 14.236-2.069z" fill="#F5BF33" p-id="5269"></path></svg> -->
                                <el-tag size="medium" color="danger">{{ role[scope.row.roleId] }}</el-tag>
                            </div>
                        </template>
                    </el-table-column>
                    
                    <el-table-column label="账号状态">
                        <template slot-scope="scope">
                            <!-- {{ scope.row.isEnabled }} -->
                            <el-switch v-model="scope.row.isEnabled" :active-value="1" :inactive-value="0" active-text="启用" inactive-text="禁用" active-color="#13ce66" inactive-color="#ff4949" style="display: block" >

                            </el-switch>
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
                    <el-option label="管理员" value="1" key="1"></el-option>
                    <el-option label="执法人员" value="2" key="2"></el-option>
                    <el-option label="普通用户" value="3" key="3"></el-option>
                    <!-- <el-option v-for="item in temp.selectOptions" :key="item.value" :label="item.label"  :value="item.value"></el-option> -->
                  </el-select>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogFormVisible = false"> 取消 </el-button>
              <el-button @click="resetForm('dataForm')"  v-if="dialogStatus=='create'">重置</el-button>
              <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
                <span v-if="dialogStatus=='create'">创建用户</span>
                <span v-if="dialogStatus=='update'">更新用户信息</span>
              </el-button>
            </div>
        </el-dialog>
    </div>

</template>
  
<script>
import axios from 'axios'
import { string } from 'jszip/lib/support';
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
                selectValue: '3',
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
            this.temp = row;
            // this.temp = Object.assign({}, row) // copy obj
            // map value of this.role to this.temp.selectValue
            // this.temp.selectValue = row.roleId
            this.temp.selectValue = String(row.roleId)
            // this.temp.selectValue=this.role[row.roleId]
            console.log(this.temp,"handleEdit")
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
                selectValue: '3',
            }
            this.$refs[formName].resetFields();
            this.dialogStatus = 'create'
            console.log("reset:",this.temp)
            // this.$refs[formName].clearValidate()
        },
        createData() {
            this.$refs['dataForm'].validate((valid) => {
            if (valid) {
                // mysql
                this.dialogFormVisible = false
                const data = {
                    username: this.temp.username,
                    password: this.temp.password,
                    email: this.temp.email,
                    roleId: this.temp.selectValue,
                }
                this.axios.post("http://127.0.0.1:8888/user/add", data,{headers: {
                    'Content-Type': 'application/json'
                }}).then(res=>{
                    this.getAllUser();
                    this.users.unshift(data);
                    console.log(this.temp)
                    console.log(res);
                    this.$notify({
                        title: 'Success',
                        message: '增加用户成功',
                        type: 'success',
                        duration: 2000
                    })
                })
            }
            })
        },
        updateData(){
            this.$refs['dataForm'].validate((valid) => {
            if (valid) {
                // mysql
                this.dialogFormVisible = false
                const data = {
                    id:this.temp.id,
                    username: this.temp.username,
                    password: this.temp.password,
                    email: this.temp.email,
                    roleId: this.temp.selectValue,
                }
                console.log('up',data);
                this.axios.post("http://127.0.0.1:8888/user/update", data,{headers: {
                    'Content-Type': 'application/json'
                }}).then(res=>{
                    console.log(this.temp)
                    console.log(res);
                    this.$notify({
                        title: 'Success',
                        message: '更新用户信息成功',
                        type: 'success',
                        duration: 2000
                    })
                }).catch(err=>{
                    console.log(err);
                    console.log(this.temp)
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
            })
        },
        
    },
    mounted(){
        this.getAllUser();
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
    /deep/.el-table td.el-table__cell div {
        height: 25px;
    }
</style>