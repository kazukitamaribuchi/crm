<template>
    <div id="customer_day_sales_analytics">
        <!-- <b-card class="customer_day_sales_analytics_area"> -->
            <b-skeleton-img
                v-if="loading"
                height="380px"
            ></b-skeleton-img>
            <div v-else>
                <b-card-text class="mb-1">
                    顧客別売上
                </b-card-text>
                <VueApexCharts
                    :height=height
                    type="bar"
                    :options="customerDaySalesChartOptions"
                    :series="customerDaySalesSeries"
                />
            </div>
        <!-- </b-card> -->
    </div>
</template>

<script>
    import dayjs from 'dayjs'
    import isBetween from 'dayjs/plugin/isBetween';
    import isSameOrAfter from 'dayjs/plugin/isSameOrAfter';
    import isSameOrBefore from 'dayjs/plugin/isSameOrBefore';
    dayjs.extend(isSameOrAfter)
    dayjs.extend(isSameOrBefore)
    dayjs.extend(isBetween)
    const now = dayjs().format('YYYY-MM-DD')

    export default {
        name: 'CustomerDaySalesAnalyticsItem',
        components: {
        },
        props: {
            height: {
                type: Number,
                required: false,
                default: 330,
            },
            targetDate: {
                type: String,
                require: false,
                default: now,
            }
        },
        data: () => ({
            customerDaySalesChartOptions: {
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
            customerDaySalesSeries: [
                {
                    name: '売上',
                    data: [44, 55, 41, 67, 22, 43]
                }
            ],
            loading: true,
        }),
        beforeCreate () {
        },
        created () {
            this.$axios({
                method: 'GET',
                url: '/api/sales/get_customer_day_sales_analytics/',
                params: {
                    target_date: this.targetDate,
                }
            })
            .then(res => {
                this.setCustomerDaySalesData(res.data)
            })
            .catch(e => {
                console.log(e)
            })
        },
        beforeMount () {
            // console.log('before mount')
        },
        mounted () {
            // console.log('mount')
        },
        beforeUpdate () {
            // console.log('before update')
        },
        update () {
            // console.log('update')
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
            setCustomerDaySalesData (item) {
                const data = item.data
                let series = []
                let categories = []
                for (const i in data) {
                    series.push(data[i].total)
                    categories.push(data[i].customer.name)
                }
                this.customerDaySalesSeries[0].data = series
                this.customerDaySalesChartOptions.xaxis.categories = categories
                this.loading = false
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    #customer_day_sales_analytics {
        max-height: 100%;
    //     .customer_day_sales_analytics_area {
    //         max-height: 100%;
    //         background-color: $theme-color;
    //         color: white;
    //     }
    }

</style>
