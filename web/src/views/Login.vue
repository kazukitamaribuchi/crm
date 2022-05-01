<template>
    <v-container
        id="login-wrap"
        fluid
    >
        <vs-row vs-justify="center">
            <vs-col
                type="flex"
                vs-justify="center"
                vs-align="center"
                vs-w="4"
            >
                <v-card

                >
                    <v-card-title
                        id="login-title"
                    >
                        Login
                    </v-card-title>
                    <v-card-text>
                        <vs-input
                            v-model="credentials.username"
                            placeholder="Username"
                        ></vs-input>
                        <vs-input
                            v-model="credentials.password"
                            placeholder="Password"
                        ></vs-input>
                        <vs-button
                            color="primary"
                            @click="login"
                        >Login</vs-button>
                    </v-card-text>
                </v-card>
            </vs-col>
        </vs-row>
    </v-container>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'LoginItem',
    data: () => ({
        credentials: {},
    }),
    created () {
        this.$axios({
            method: 'GET',
            url: 'api/customer/',
        })
        .then(res => {
            console.log(res)
        })
        .catch(e => {
            console.log(e)
        })
    },
    methods: {
        ...mapActions([
            'checkAuthToken',
        ]),
        login () {
            console.log(this.credentials)
            this.checkAuthToken(this.credentials)
            .then(res => {
                console.log('ログイン成功や')
                this.$router.push({name: 'Home'})
            })
            .catch(e => {
                console.log('ログイン失敗や')
            })
        }
    }
}
</script>

<style lang="scss" scoped>
#login-wrap {
    font-family: Hiragino Kaku Gothic Pro,ヒラギノ角ゴ Pro,Yu Gothic Medium,游ゴシック Medium,YuGothic,游ゴシック体,メイリオ,sans-serif;

    .vs-component.vs-con-input-label.vs-input.vs-input-primary::v-deep {
        width: 100%;
    }
    .vs-input-parent::v-deep {
        width: 100%;
        .vs-input {
            width: 100%;
        }
    }
}
</style>
