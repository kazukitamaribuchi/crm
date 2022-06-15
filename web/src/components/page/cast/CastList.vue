<template>
    <div id="cast_list_wrap">
        <b-row>
            <b-tabs pill card>
                <b-tab
                    title="管理画面"
                    :active=topActive
                    @click="setCastTopActive(0)"
                >
                    <b-row>
                        <b-col cols="3" style="max-height: 100%;">
                            <b-card class="cast_list_area" style="height: 48%;">
                                <b-container fluid>
                                    <b-card-text class="mb-1">
                                        在籍キャスト
                                    </b-card-text>
                                    <b-row>
                                        <b-col cols="8">
                                            <VueApexCharts
                                                width="160"
                                                height="160"
                                                type="radialBar"
                                                :options="totalCastChartOptions"
                                                :series="totalCastSeries"
                                            />
                                        </b-col>
                                        <b-col cols="4" align="right" class="pt-5 ml-0 pl-0">
                                            <b-card-title>
                                                {{ totalCast }}
                                            </b-card-title>
                                            <b-card-sub-title>
                                                casts
                                            </b-card-sub-title>
                                        </b-col>
                                    </b-row>
                                </b-container>
                            </b-card>
                            <b-card class="cast_list_area" style="height: 48%; margin-top: 15px;">
                                <b-container fluid>
                                    <b-card-text class="mb-1">
                                        平均年齢
                                    </b-card-text>
                                    <b-row>
                                        <b-col cols="8">
                                            <VueApexCharts
                                                width="155"
                                                height="155"
                                                type="radialBar"
                                                :options="castAverageAgeChartOptions"
                                                :series="castAverageAgeSeries"
                                            />
                                        </b-col>
                                        <b-col cols="4" align="right" class="pt-5">
                                            <b-card-title>
                                                24
                                            </b-card-title>
                                            <b-card-sub-title>
                                                age
                                            </b-card-sub-title>
                                        </b-col>
                                    </b-row>
                                </b-container>
                            </b-card>
                        </b-col>
                        <b-col cols="5" style="max-height: 100%;">
                            <b-card class="cast_list_area">
                                <b-container fluid>
                                    <b-card-text class="mb-3 mt-3">
                                        キャスト別売上
                                    </b-card-text>
                                    <VueApexCharts
                                        height="365"
                                        width="420"
                                        type="bar"
                                        :options="castSalesRankingChartOptions"
                                        :series="castSalesRankingSeries"
                                    />
                                </b-container>
                            </b-card>
                        </b-col>
                        <b-col cols="4" style="max-height: 100%;">
                            <b-card
                                class="cast_list_area"
                                header="売上ランキング（全期間）"
                                header-bg-variant="dark"
                                header-text-variant="white"
                                header-class="cast_list_area_rank_header"
                                body-class="cast_list_area_rank_body"
                            >
                                <b-row class="cast_list_area_rank_top mb-2">
                                    <b-col cols="5">
                                        名前
                                    </b-col>
                                    <b-col cols="3" align="right">
                                        指名回数
                                    </b-col>
                                    <b-col cols="4" align="right">
                                        売上
                                    </b-col>
                                </b-row>
                                <b-row
                                    v-for="(item, i) in castSalesRanking"
                                    :key=i
                                    class="cast_list_area_rank_middle mb-0 mt-0"
                                >
                                    <b-col cols="5">
                                        <b-card-text><img
                                            src="@/assets/img/女性11.jpg"
                                            class="cast_list_area_sales_rank_cast_icon"
                                        > {{ item.name }}</b-card-text>
                                    </b-col>
                                    <b-col cols="3" align="right">
                                        {{ item.total_appoint }} 回
                                    </b-col>
                                    <b-col cols="4" align="right">
                                        <b-icon icon="currency-yen"></b-icon>
                                        <b>{{ item.total_sales }}</b>
                                    </b-col>
                                </b-row>
                            </b-card>
                        </b-col>

                    </b-row>
                    <b-row>
                        <b-col cols="6">
                            <b-card class="cast_list_area">
                                <b-container fluid>
                                    <b-card-text class="mb-1 pt-3">
                                        年齢分布
                                    </b-card-text>
                                    <VueApexCharts
                                        height="250"
                                        type="bar"
                                        :options="castAgeChartOptions"
                                        :series="castAgeSeries"
                                    />
                                </b-container>
                            </b-card>
                        </b-col>
                        <b-col cols="6">
                            <b-card class="cast_list_area">
                                <b-container fluid>
                                    <b-card-text class="mb-1 pt-3">
                                        勤続年数
                                    </b-card-text>
                                    <VueApexCharts
                                        height="250"
                                        type="bar"
                                        :options="castServiceYearChartOptions"
                                        :series="castServiceYearSeries"
                                    />
                                </b-container>
                            </b-card>
                        </b-col>
                    </b-row>
                </b-tab>
                <b-tab
                    title="キャスト一覧"
                    :active=!topActive
                    @click="setCastTopActive(1)"
                >
                    <!-- <b-card class="cast_list_area"> -->

                        <b-row>
                            <b-col
                                cols="3"
                                v-for="item in filterdCast"
                                :key=item.id
                            >
                                <b-card
                                    @click="showCastDetail"
                                    style="cursor: pointer;"
                                >
                                <!-- bg-variant="dark"
                                text-variant="white" -->
                                    <b-row>
                                        <b-col cols="6">
                                            <img
                                                src="@/assets/img/女性11.jpg"
                                                class="cast_list_area_cast_icon"
                                                top
                                            >
                                        </b-col>
                                        <b-col cols="5" align="right">
                                            <b-card-title class="mt-4">
                                                {{ item.name }}
                                            </b-card-title>
                                            <b-card-sub-title>
                                                {{ item.age }}
                                            </b-card-sub-title>
                                        </b-col>
                                        <b-col></b-col>
                                    </b-row>
                                </b-card>
                            </b-col>
                        </b-row>
                    <!-- </b-card> -->
                </b-tab>
            </b-tabs>
        </b-row>
    </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'
import _ from 'lodash'
import dayjs from 'dayjs'
import isBetween from 'dayjs/plugin/isBetween';
import isSameOrAfter from 'dayjs/plugin/isSameOrAfter';
import isSameOrBefore from 'dayjs/plugin/isSameOrBefore';
dayjs.extend(isSameOrAfter)
dayjs.extend(isSameOrBefore)
dayjs.extend(isBetween)

export default {
    name: 'CastListItem',
    data: () => ({
        filterdCast: [],
        searchWord: '',
        defaultIcon: 'http://localhost:8000/media/upload/女性1111.png',
        apiPath: 'http://localhost:8000',
        totalCastChartOptions: {
            chart: {
              height: 350,
              type: 'radialBar',
              toolbar: {
                show: false
              }
            },
            plotOptions: {
              radialBar: {
                startAngle: -135,
                endAngle: 225,
                 hollow: {
                  margin: 0,
                  size: '80%',
                  background: '#fff',
                  image: undefined,
                  imageOffsetX: 0,
                  imageOffsetY: 0,
                  position: 'front',
                  dropShadow: {
                    enabled: true,
                    top: 3,
                    left: 0,
                    blur: 4,
                    opacity: 0.24
                  }
                },
                track: {
                  background: '#fff',
                  strokeWidth: '67%',
                  margin: 0, // margin is in pixels
                  dropShadow: {
                    enabled: true,
                    top: -3,
                    left: 0,
                    blur: 4,
                    opacity: 0.35
                  }
                },

                dataLabels: {
                  show: true,
                  name: {
                    offsetY: -10,
                    show: true,
                    color: '#888',
                    fontSize: '17px'
                  },
                  value: {
                    formatter: function(val) {
                      return parseInt(val);
                    },
                    color: '#111',
                    fontSize: '20px',
                    show: true,
                  }
                }
              }
            },
            fill: {
              type: 'gradient',
              gradient: {
                shade: 'dark',
                type: 'horizontal',
                shadeIntensity: 0.5,
                gradientToColors: ['#ABE5A1'],
                inverseColors: true,
                opacityFrom: 1,
                opacityTo: 1,
                stops: [0, 100]
              }
            },
            stroke: {
              lineCap: 'round'
            },
            labels: ['total'],
        },
        totalCast: 0,
        castAverageAgeChartOptions: {
            chart: {
              height: 350,
              type: 'radialBar',
              toolbar: {
                show: false
              }
            },
            plotOptions: {
              radialBar: {
                startAngle: -135,
                endAngle: 225,
                 hollow: {
                  margin: 0,
                  size: '80%',
                  background: '#fff',
                  image: undefined,
                  imageOffsetX: 0,
                  imageOffsetY: 0,
                  position: 'front',
                  dropShadow: {
                    enabled: true,
                    top: 3,
                    left: 0,
                    blur: 4,
                    opacity: 0.24
                  }
                },
                track: {
                  background: '#fff',
                  strokeWidth: '67%',
                  margin: 0, // margin is in pixels
                  dropShadow: {
                    enabled: true,
                    top: -3,
                    left: 0,
                    blur: 4,
                    opacity: 0.35
                  }
                },

                dataLabels: {
                  show: true,
                  name: {
                    offsetY: -10,
                    show: true,
                    color: '#888',
                    fontSize: '17px'
                  },
                  value: {
                    formatter: function(val) {
                      return parseInt(val);
                    },
                    color: '#111',
                    fontSize: '20px',
                    show: true,
                  }
                }
              }
            },
            // fill: {
            //   type: 'gradient',
            //   gradient: {
            //     shade: 'dark',
            //     type: 'horizontal',
            //     shadeIntensity: 0.5,
            //     gradientToColors: ['#ABE5A1'],
            //     inverseColors: true,
            //     opacityFrom: 1,
            //     opacityTo: 1,
            //     stops: [0, 100]
            //   }
            // },
            stroke: {
              lineCap: 'round'
            },
            labels: ['active'],
        },
        currentPage: 1,
        totalRows: 1,
        perPage: 15,
        filter: null,
        filterOn: [],
        castAgeChartOptions: {
            chart: {
                height: 350,
                type: 'bar',
            },
            plotOptions: {
                bar: {
                    borderRadius: 10,
                    dataLabels: {
                        position: 'top', // top, center, bottom
                    },
                }
            },
            dataLabels: {
                enabled: true,
                formatter: function (val) {
                    return val + "%";
                },
                offsetY: -20,
                style: {
                    fontSize: '12px',
                    colors: ["#304758"]
                }
            },
            xaxis: {
                categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                position: 'top',
                axisBorder: {
                    show: false
                },
                axisTicks: {
                    show: false
                },
                crosshairs: {
                    fill: {
                        type: 'gradient',
                        gradient: {
                            colorFrom: '#D8E3F0',
                            colorTo: '#BED1E6',
                            stops: [0, 100],
                            opacityFrom: 0.4,
                            opacityTo: 0.5,
                        }
                    }
                },
                tooltip: {
                    enabled: true,
                }
            },
            yaxis: {
                axisBorder: {
                    show: false
                },
                axisTicks: {
                    show: false,
                },
                labels: {
                    show: false,
                    formatter: function (val) {
                      return val + "%";
                    }
                }
            },
            title: {
                text: 'Monthly Inflation in Argentina, 2002',
                floating: true,
                offsetY: 330,
                align: 'center',
                style: {
                    color: '#444'
                }
            }
        },
        castAgeSeries: [
            {
                name: 'Inflation',
                data: [2.3, 3.1, 4.0, 10.1, 4.0, 3.6, 3.2, 2.3, 1.4, 0.8, 0.5, 0.2]
            }
        ],
        castServiceYearChartOptions: {
            chart: {
                type: 'bar',
                height: 250
            },
            plotOptions: {
                bar: {
                    horizontal: false,
                    columnWidth: '55%',
                    endingShape: 'rounded'
                },
            },
            colors: ['#00E396'],
            dataLabels: {
                enabled: false
            },
            stroke: {
                show: true,
                width: 2,
                colors: ['transparent']
            },
            xaxis: {
              categories: ['愛理', '理沙', '美鈴', '絵美', '樹里亜'],
            },
            yaxis: {
              title: {
                text: '勤続年数(ヵ月)'
              }
            },
            fill: {
              opacity: 1
            },
            tooltip: {
              y: {
                formatter: function (val) {
                  return val + " ヵ月"
                }
              }
          },
          legend: {
              show: true,
              showForSingleSeries: true,
              customLegendItems: ['勤続年数'],
              markers: {
                fillColors: ['#00E396']
              }
            }
        },
        castServiceYearSeries: [
            {
                name: '勤続年数',
                data: [0.5, 13, 7, 2, 3]
            }
        ],
        castSalesRankingSeries: [
            {
                data: [10, 220, 340, 120, 30, 1240]
            }
        ],
        castSalesRankingChartOptions: {
            chart: {
              type: 'bar',
              events: {
                click: function(chart, w, e) {
                  console.log(chart, w, e)
                }
              }
            },
            plotOptions: {
              bar: {
                columnWidth: '45%',
                distributed: true,
              }
            },
            dataLabels: {
              enabled: false
            },
            legend: {
              show: false
            },
            colors: ['#33b2df', '#546E7A', '#d4526e', '#13d8aa', '#A5978B', '#A5978B'],
            xaxis: {
              categories: [
                ['愛理'],
                ['理沙'],
                ['美鈴'],
                '絵美',
                ['奈津美'],
                ['里奈'],
              ],
              labels: {
                style: {
                  colors: ['#33b2df', '#546E7A', '#d4526e', '#13d8aa', '#A5978B', '#A5978B'],
                  fontSize: '12px'
                }
              }
            }
        },
        castSalesRanking: [
            {
                name: '愛理',
                total_sales: 99999999,
                total_appoint: 240,
            },
            {
                name: '愛理',
                total_sales: 99999999,
                total_appoint: 240,
            },
            {
                name: '愛理',
                total_sales: 99999999,
                total_appoint: 240,
            },
            {
                name: '愛理',
                total_sales: 99999999,
                total_appoint: 240,
            },
            {
                name: '愛理',
                total_sales: 99999999,
                total_appoint: 240,
            },
        ]
    }),
    computed: {
        ...mapGetters([
            'cast',
            'castTopActive',
        ]),
        topActive () {
            if (this.castTopActive == undefined || this.castTopActive == 0) {
                return true
            }
            return false
        },
        totalCastSeries () {
            return [5]
        },
        castAverageAgeSeries () {
            return [6]
        },
    },
    created () {
        this.getCastList()
        .then(res => {
            this.setCastList(res)
            this.filterdCast = _.cloneDeep(res.data)
        })
    },
    mounted () {
        console.log('this.cast', this.cast)
        this.totalCast = this.cast.length
        this.totalRows = this.cast.length
    },
    methods: {
        ...mapMutations([
            'setCastList',
            'setCastTopActive',
        ]),
        ...mapActions([
            'getCastList',
        ]),
        showCastDetail () {

        },
    }
}
</script>

<style lang="scss" scoped>
    #cast_list_wrap {
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        // height: $main-height;
        padding: 20px;

        .cast_list_area {
            background-color: $theme-color;
            color: white;
        }

        .cast_list_area_rank_header {
            text-align: center;
            padding: 15px;
        }

        .cast_list_area_rank_body {
            margin-top: 0;
            padding-top: 0;
        }

        .cast_list_area_sales_rank_cast_icon {
            border-radius: 50%;
            width: 45px;
            height: 45px;
        }

        .cast_list_area_cast_icon {
            border-radius: 50%;
            width: 140px;
            height: 140px;
            // box-shadow: 1px 1px 2px 1px rgba(100, 100, 100, 0.5);
            // border: 1px solid rgba(100, 100, 100, 0.3);
        }

    }
    .card-header {
        background-color: $theme-color !important;
        border-bottom: 0px !important;
    }
</style>
