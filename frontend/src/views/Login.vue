<template>
  <v-container fluid class="fill-height bg-gradient">
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card class="elevation-12">
          <v-card-title class="text-center bg-primary pa-6">
            <h2 class="text-white">文章管理系统</h2>
          </v-card-title>

          <v-card-text class="pa-6">
            <v-form ref="formRef" v-model="valid" @submit.prevent="handleLogin">
              <v-text-field
                v-model="form.username"
                label="用户名"
                prepend-inner-icon="mdi-account"
                :rules="[rules.required]"
                variant="outlined"
                class="mb-3"
              ></v-text-field>

              <v-text-field
                v-model="form.password"
                label="密码"
                prepend-inner-icon="mdi-lock"
                :rules="[rules.required]"
                :type="showPassword ? 'text' : 'password'"
                :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append-inner="showPassword = !showPassword"
                variant="outlined"
                class="mb-3"
              ></v-text-field>

              <v-alert
                v-if="error"
                type="error"
                density="compact"
                class="mb-3"
              >
                {{ error }}
              </v-alert>

              <v-btn
                type="submit"
                color="primary"
                block
                size="large"
                :loading="loading"
                :disabled="!valid"
              >
                登录
              </v-btn>
            </v-form>
          </v-card-text>

          <v-card-actions class="pa-6 pt-0">
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              @click="$router.push('/register')"
            >
              还没有账号？去注册
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const formRef = ref(null)
const valid = ref(false)
const loading = ref(false)
const error = ref('')
const showPassword = ref(false)

const form = ref({
  username: '',
  password: ''
})

const rules = {
  required: value => !!value || '此字段必填'
}

const handleLogin = async () => {
  if (!valid.value) return

  loading.value = true
  error.value = ''

  const result = await authStore.login(form.value)

  if (result.success) {
    router.push('/dashboard')
  } else {
    error.value = result.error
  }

  loading.value = false
}
</script>

<style scoped>
.bg-gradient {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
</style>
