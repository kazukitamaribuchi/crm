<template>
    <div id="customer_sales_analytics">
        <b-card class="customer_sales_analytics_area">
            <b-card-text class="mb-1">
                顧客別売上(test)
            </b-card-text>
            <VueApexCharts
                :height=height
                type="bar"
                :options="customerSalesChartOptions"
                :series="customerSalesSeries"
            />
        </b-card>
    </div>
</template>
<script>
    export default {
        name: 'CustomerSalesItem',
        components: {
        },
        props: {
            height: {
                type: Number,
                required: false,
                default: 330,
            },
            target: {
                type: Number,
                require: false,
                default: 0,
            }
        },
        data: () => ({
            customerSalesChartOptions: {
                chart: {
                  type: 'bar',
                  height: 350,
                  stacked: true,
                  toolbar: {
                    show: true
                  },
                  zoom: {
                    enabled: true
                  }
                },
                responsive: [{
                  breakpoint: 480,
                  options: {
                    legend: {
                      position: 'bottom',
                      offsetX: -10,
                      offsetY: 0
                    }
                  }
                }],
                plotOptions: {
                  bar: {
                    horizontal: false,
                    borderRadius: 10
                  },
                },
                xaxis: {
                  categories: ['斎藤一', '斎藤一1', '斎藤一2', '斎藤一3', '斎藤一4', '斎藤一5'],
                },
                legend: {
                  position: 'right',
                  offsetY: 40
                },
                fill: {
                  opacity: 1
                }
            },
            customerSalesSeries: [
                {
                name: 'PRODUCT A',
                data: [44, 55, 41, 67, 22, 43]
                }, {
                name: 'PRODUCT B',
                data: [13, 23, 20, 8, 13, 27]
                }, {
                name: 'PRODUCT C',
                data: [11, 17, 15, 15, 21, 14]
                }, {
                name: 'PRODUCT D',
                data: [21, 7, 25, 13, 22, 8]
                }
            ],
        }),
        beforeCreate () {
        },
        created () {
            this.$axios({
                method: 'GET',
                url: '/api/sales/get_customer_sales_analytics/',
                data: {
                    'target': this.target,
                }
            })
            .then(res => {
                console.log(res)
            })
            .catch(e => {
                console.log(e)
            })
        },
        beforeMount () {
        },
        mounted () {
        },
        beforeUpdate () {
        },
        update () {
        },
        beforeDestroy () {
        },
        destoryd () {
        },
        watch: {
        },
        computed: {
        },
        methods: {
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    .customer_sales_analytics_area {
        background-color: $theme-color;
        color: white;
    }
</style>
