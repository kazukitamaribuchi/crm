<template>
    <div id="sales_list_wrap">
        <b-row>
            <b-tabs pill card>
                <b-tab
                    title="管理画面"
                    :active=topActive
                    @click="setSalesTopActive(0)"
                >
                    <b-tabs pills card fill>
                        <b-tab title="本日" active>
                            <b-row class="sales_list_area_top">
                                <b-col cols="8" class="sales_list_area_top_left pb-2">
                                    <b-card class="sales_list_area">
                                        <b-card-text class="mb-1">
                                            顧客別売上
                                        </b-card-text>
                                        <VueApexCharts
                                            height="330"
                                            type="bar"
                                            :options="customerSalesChartOptions"
                                            :series="customerSalesSeries"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="4" class="sales_list_area_top_right">
                                    <b-card class="sales_list_area sales_list_area_top_right1">
                                        <b-container fluid>
                                            <!-- <b-card-text class="mb-1">
                                                総売上
                                            </b-card-text>
                                            <b-card-sub-title>
                                                (本日)
                                            </b-card-sub-title>
                                            <b-card-text align="center" style="font-size: 20px;">
                                                ￥1,243,200
                                            </b-card-text>
                                            <VueApexCharts
                                                height="150"
                                                type="area"
                                                :options="totalSalesChartOptions2"
                                                :series="totalSalesSeries2"
                                            /> -->
                                            <b-card-text class="mb-1">
                                                総売上 (本日)
                                            </b-card-text>
                                            <b-row>
                                                <b-col cols="6">
                                                    <VueApexCharts
                                                        width="150"
                                                        height="150"
                                                        type="radialBar"
                                                        :options="totalSalesChartOptions"
                                                        :series=[129]
                                                    />
                                                </b-col>
                                                <b-col cols="6" align="right" class="pt-4 ml-0 pl-0">
                                                    <b-card-title class="total_sales_content mt-2">
                                                        ￥1,298,400
                                                    </b-card-title>
                                                    <b-card-sub-title>
                                                        sales
                                                    </b-card-sub-title>
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                    <b-card class="sales_list_area sales_list_area_top_right2">
                                        <b-container fluid>
                                            <b-card-text class="mb-1">
                                                総来店数 (本日)
                                            </b-card-text>
                                            <b-row>
                                                <b-col cols="6">
                                                    <VueApexCharts
                                                        width="150"
                                                        height="150"
                                                        type="radialBar"
                                                        :options="totalSalesChartOptions"
                                                        :series="[8]"
                                                    />
                                                </b-col>
                                                <b-col cols="6" align="right" class="pt-4 ml-0 pl-0">
                                                    <b-card-title class="mt-2">
                                                        8
                                                    </b-card-title>
                                                    <b-card-sub-title>
                                                        customers
                                                    </b-card-sub-title>
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                </b-col>
                            </b-row>
                            <b-row class="sales_list_area_middle">
                                <b-col cols="3">
                                    <b-card class="sales_list_area sales_list_area_middle_left">
                                        <b-card-text>
                                            基本プラン比率
                                        </b-card-text>
                                        <VueApexCharts
                                            height="200"
                                            type="pie"
                                            :options="normalVipChartOptions"
                                            :series="[90, 10]"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="3">
                                    <b-card class="sales_list_area sales_list_area_middle_left">
                                        <b-card-text>
                                            指名比率
                                        </b-card-text>
                                        <VueApexCharts
                                            height="200"
                                            type="pie"
                                            :options="appointTypeChartOptions"
                                            :series="[75, 25]"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="6">
                                    <b-card class="sales_list_area">
                                        <b-card-text>
                                            キャスト別売上
                                        </b-card-text>
                                        <VueApexCharts
                                            height="200"
                                            type="bar"
                                            :options="appointChartOptions"
                                            :series="appointSeries"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                            <b-row>
                                <b-col cols="7">
                                    <b-card class="sales_list_area">
                                        <b-card-text class="mb-1">
                                            商品別売上
                                        </b-card-text>
                                        <VueApexCharts
                                            height="250"
                                            type="bar"
                                            :options="productSalesChartOptions"
                                            :series="productSalesSeries"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="5">
                                    <b-card class="sales_list_area">
                                        <b-card-text class="mb-1">
                                            顧客別滞在時間
                                        </b-card-text>
                                        <VueApexCharts
                                            height="250"
                                            type="rangeBar"
                                            :options="visitTimeChartOptions"
                                            :series="visitTimeSeries"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                        </b-tab>
                        <b-tab title="前日">
                            <b-row class="sales_list_area_top">
                                <b-col cols="8" class="sales_list_area_top_left pb-2">
                                    <b-card class="sales_list_area">
                                        <b-card-text class="mb-1">
                                            顧客別売上
                                        </b-card-text>
                                        <VueApexCharts
                                            height="330"
                                            type="bar"
                                            :options="customerSalesChartOptions"
                                            :series="customerSalesSeries"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="4" class="sales_list_area_top_right">
                                    <b-card class="sales_list_area sales_list_area_top_right1">
                                        <b-container fluid>
                                            <b-card-text class="mb-1">
                                                総売上 (前日)
                                            </b-card-text>
                                            <b-row>
                                                <b-col cols="6">
                                                    <VueApexCharts
                                                        width="150"
                                                        height="150"
                                                        type="radialBar"
                                                        :options="totalSalesChartOptions"
                                                        :series=[129]
                                                    />
                                                </b-col>
                                                <b-col cols="6" align="right" class="pt-4 ml-0 pl-0">
                                                    <b-card-title class="total_sales_content mt-2">
                                                        ￥1,298,400
                                                    </b-card-title>
                                                    <b-card-sub-title>
                                                        sales
                                                    </b-card-sub-title>
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                    <b-card class="sales_list_area sales_list_area_top_right2">
                                        <b-container fluid>
                                            <b-card-text class="mb-1">
                                                総来店数 (前日)
                                            </b-card-text>
                                            <b-row>
                                                <b-col cols="6">
                                                    <VueApexCharts
                                                        width="150"
                                                        height="150"
                                                        type="radialBar"
                                                        :options="totalSalesChartOptions"
                                                        :series="[8]"
                                                    />
                                                </b-col>
                                                <b-col cols="6" align="right" class="pt-4 ml-0 pl-0">
                                                    <b-card-title class="mt-2">
                                                        8
                                                    </b-card-title>
                                                    <b-card-sub-title>
                                                        customers
                                                    </b-card-sub-title>
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                </b-col>
                            </b-row>
                            <b-row class="sales_list_area_middle">
                                <b-col cols="3">
                                    <b-card class="sales_list_area sales_list_area_middle_left">
                                        <b-card-text>
                                            基本プラン比率
                                        </b-card-text>
                                        <VueApexCharts
                                            height="200"
                                            type="pie"
                                            :options="normalVipChartOptions"
                                            :series="[90, 10]"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="3">
                                    <b-card class="sales_list_area sales_list_area_middle_left">
                                        <b-card-text>
                                            指名比率
                                        </b-card-text>
                                        <VueApexCharts
                                            height="200"
                                            type="pie"
                                            :options="appointTypeChartOptions"
                                            :series="[75, 25]"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="6">
                                    <b-card class="sales_list_area">
                                        <b-card-text>
                                            キャスト別売上
                                        </b-card-text>
                                        <VueApexCharts
                                            height="200"
                                            type="bar"
                                            :options="appointChartOptions"
                                            :series="appointSeries"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                            <b-row>
                                <b-col cols="7">
                                    <b-card class="sales_list_area">
                                        <b-card-text class="mb-1">
                                            商品別売上
                                        </b-card-text>
                                        <VueApexCharts
                                            height="250"
                                            type="bar"
                                            :options="productSalesChartOptions"
                                            :series="productSalesSeries"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="5">
                                    <b-card class="sales_list_area">
                                        <b-card-text class="mb-1">
                                            顧客別滞在時間
                                        </b-card-text>
                                        <VueApexCharts
                                            height="250"
                                            type="rangeBar"
                                            :options="visitTimeChartOptions"
                                            :series="visitTimeSeries"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                        </b-tab>
                        <b-tab title="週">
                            <b-row>
                                <b-col cols="8">
                                    <b-card class="sales_list_area sales_list_area1">
                                        <b-container fluid>
                                            <b-card-text class="">
                                                週売上
                                            </b-card-text>
                                            <b-row>
                                                <b-col>
                                                    <VueApexCharts
                                                        height="300"
                                                        :options="salesEachPeriodChartOptions"
                                                        :series="salesEachPeriodSeries"
                                                    />
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                </b-col>
                                <b-col cols="4">
                                    <b-card class="sales_list_area sales_list_area_top_right1">
                                        <b-container fluid>
                                            <!-- <b-card-text class="mb-1">
                                                総売上
                                            </b-card-text>
                                            <b-card-sub-title>
                                                (本日)
                                            </b-card-sub-title>
                                            <b-card-text align="center" style="font-size: 20px;">
                                                ￥1,243,200
                                            </b-card-text>
                                            <VueApexCharts
                                                height="150"
                                                type="area"
                                                :options="totalSalesChartOptions2"
                                                :series="totalSalesSeries2"
                                            /> -->
                                            <b-card-text class="mb-1">
                                                総売上 (週)
                                            </b-card-text>
                                            <b-row>
                                                <b-col cols="6">
                                                    <VueApexCharts
                                                        width="150"
                                                        height="150"
                                                        type="radialBar"
                                                        :options="totalSalesChartOptions"
                                                        :series=[129]
                                                    />
                                                </b-col>
                                                <b-col cols="6" align="right" class="pt-4 ml-0 pl-0">
                                                    <b-card-title class="total_sales_content mt-2">
                                                        ￥1,298,400
                                                    </b-card-title>
                                                    <b-card-sub-title>
                                                        sales
                                                    </b-card-sub-title>
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                    <b-card class="sales_list_area sales_list_area_top_right2">
                                        <b-container fluid>
                                            <b-card-text class="mb-1">
                                                総来店数 (週)
                                            </b-card-text>
                                            <b-row>
                                                <b-col cols="6">
                                                    <VueApexCharts
                                                        width="150"
                                                        height="150"
                                                        type="radialBar"
                                                        :options="totalSalesChartOptions"
                                                        :series="[8]"
                                                    />
                                                </b-col>
                                                <b-col cols="6" align="right" class="pt-4 ml-0 pl-0">
                                                    <b-card-title class="mt-2">
                                                        8
                                                    </b-card-title>
                                                    <b-card-sub-title>
                                                        customers
                                                    </b-card-sub-title>
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                </b-col>
                            </b-row>
                        </b-tab>
                        <b-tab title="月">
                            <b-row>
                                <b-col cols="8">
                                    <b-card class="sales_list_area sales_list_area1">
                                        <b-container fluid>
                                            <b-card-text class="">
                                                月売上
                                            </b-card-text>
                                            <b-row>
                                                <b-col>
                                                    <VueApexCharts
                                                        height="300"
                                                        :options="salesEachPeriodChartOptions"
                                                        :series="salesEachPeriodSeries"
                                                    />
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                </b-col>
                                <b-col cols="4">
                                    <b-card class="sales_list_area sales_list_area_top_right1">
                                        <b-container fluid>
                                            <!-- <b-card-text class="mb-1">
                                                総売上
                                            </b-card-text>
                                            <b-card-sub-title>
                                                (本日)
                                            </b-card-sub-title>
                                            <b-card-text align="center" style="font-size: 20px;">
                                                ￥1,243,200
                                            </b-card-text>
                                            <VueApexCharts
                                                height="150"
                                                type="area"
                                                :options="totalSalesChartOptions2"
                                                :series="totalSalesSeries2"
                                            /> -->
                                            <b-card-text class="mb-1">
                                                総売上 (月)
                                            </b-card-text>
                                            <b-row>
                                                <b-col cols="6">
                                                    <VueApexCharts
                                                        width="150"
                                                        height="150"
                                                        type="radialBar"
                                                        :options="totalSalesChartOptions"
                                                        :series=[129]
                                                    />
                                                </b-col>
                                                <b-col cols="6" align="right" class="pt-4 ml-0 pl-0">
                                                    <b-card-title class="total_sales_content mt-2">
                                                        ￥1,298,400
                                                    </b-card-title>
                                                    <b-card-sub-title>
                                                        sales
                                                    </b-card-sub-title>
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                    <b-card class="sales_list_area sales_list_area_top_right2">
                                        <b-container fluid>
                                            <b-card-text class="mb-1">
                                                総来店数 (月)
                                            </b-card-text>
                                            <b-row>
                                                <b-col cols="6">
                                                    <VueApexCharts
                                                        width="150"
                                                        height="150"
                                                        type="radialBar"
                                                        :options="totalSalesChartOptions"
                                                        :series="[8]"
                                                    />
                                                </b-col>
                                                <b-col cols="6" align="right" class="pt-4 ml-0 pl-0">
                                                    <b-card-title class="mt-2">
                                                        8
                                                    </b-card-title>
                                                    <b-card-sub-title>
                                                        customers
                                                    </b-card-sub-title>
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                </b-col>
                            </b-row>
                        </b-tab>
                        <b-tab title="年" disabled>
                        </b-tab>
                    </b-tabs>


                    <!-- <b-row>
                        <b-col cols="7">
                            <b-card class="sales_list_area sales_list_1">
                                <b-container fluid>
                                    <b-card-text class="">
                                        売上/来店数
                                    </b-card-text>
                                    <b-row>
                                        <b-col>
                                            <VueApexCharts
                                                height="300"
                                                :options="salesVisitChartOptions"
                                                :series="salesVisitSeries"
                                            />
                                        </b-col>
                                    </b-row>
                                </b-container>
                            </b-card>
                        </b-col>
                        <b-col>
                            <b-card class="sales_list_area sales_list_2">
                            </b-card>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col cols="3">
                            <b-card class="sales_list_area sales_list_3">
                            </b-card>
                        </b-col>
                        <b-col cols="6">
                            <b-card class="sales_list_area sales_list_4">
                            </b-card>
                        </b-col>
                        <b-col>
                            <b-card class="sales_list_area sales_list_5">
                            </b-card>
                        </b-col>
                    </b-row> -->
                </b-tab>
                <b-tab
                    title="売上一覧"
                    :active=!topActive
                    @click="setSalesTopActive(1)"
                >
                    <v-row>
                        <b-table
                            hover
                            :items="sales"
                            :fields="fields"
                            dark
                            caption-top
                            selectable
                            :per-page="perPage"
                            :current-page="currentPage"
                            :filter="filter"
                            :filter-included-fields="filterOn"
                            @row-selected="onRowSelected"
                        >
                            <template #cell(appoint)="data">
                                <b v-if="data.value">
                                    有
                                </b>
                                <b v-else>
                                    フリー
                                </b>
                            </template>

                            <template #cell(douhan)="data">
                                <b v-if="data.value">
                                    有
                                </b>
                                <b v-else>
                                    無
                                </b>
                            </template>
                        </b-table>
                    </v-row>
                </b-tab>
            </b-tabs>
        </b-row>

        <!-- <InputSalesDialog
            @update="inputSalesDialog = $event"
            :inputSalesDialog="inputSalesDialog"
        /> -->
    </div>
</template>

<script>
import InputSalesDialog from '@/components/common/dialog/InputSalesDialog'
import { mapGetters, mapMutations, mapActions } from 'vuex'
import dayjs from 'dayjs'
import isBetween from 'dayjs/plugin/isBetween';
import isSameOrAfter from 'dayjs/plugin/isSameOrAfter';
import isSameOrBefore from 'dayjs/plugin/isSameOrBefore';
dayjs.extend(isSameOrAfter)
dayjs.extend(isSameOrBefore)
dayjs.extend(isBetween)
// dayjs.extend(require('dayjs/plugin/timezone'))
// dayjs.extend(require('dayjs/plugin/utc'))
// dayjs.tz.setDefault('Asia/Tokyo')

export default {
    name: 'SalesListItem',
    data: () => ({
        inputSalesDialog: false,
        salesVisitSeries: [
            {
                name: 'Website Blog',
                type: 'column',
                data: [440, 505, 414, 671, 227, 413, 201, 352, 752, 320, 257, 160]
            },
            {
                name: 'Social Media',
                type: 'line',
                data: [23, 42, 35, 27, 43, 22, 17, 31, 22, 22, 12, 16]
            }
        ],
        salesVisitChartOptions: {
            chart: {
                height: 350,
                type: 'line',
            },
            stroke: {
                width: [0, 4]
            },
            title: {
                text: 'Traffic Sources'
            },
            dataLabels: {
                enabled: true,
                enabledOnSeries: [1]
            },
            labels: ['01 Jan 2001', '02 Jan 2001', '03 Jan 2001', '04 Jan 2001', '05 Jan 2001', '06 Jan 2001', '07 Jan 2001', '08 Jan 2001', '09 Jan 2001', '10 Jan 2001', '11 Jan 2001', '12 Jan 2001'],
            xaxis: {
                type: 'datetime'
            },
            yaxis: [{
                title: {
                    text: 'Website Blog',
                },
            }, {
                opposite: true,
                title: {
                    text: 'Social Media'
                }
            }]
        },
        salesEachPeriodSeries: [
            {
              data: [
                  8107.85,
                  8128.0,
                  8122.9,
                  8165.5,
                  8340.7,
                  8423.7,
                  8423.5,
                  8514.3,
                  8481.85,
                  8487.7,
                  8506.9,
                  8626.2,
                  8668.95,
                  8602.3,
                  8607.55,
                  8512.9,
                  8496.25,
                  8600.65,
                  8881.1,
                  9340.85
                ],
            },
        ],
        salesEachPeriodChartOptions: {
            chart: {
              height: 350,
              type: 'line',
              id: 'areachart-2'
            },
            annotations: {
              yaxis: [{
                y: 8200,
                borderColor: '#00E396',
                label: {
                  borderColor: '#00E396',
                  style: {
                    color: '#fff',
                    background: '#00E396',
                  },
                  text: 'Support',
                }
              }, {
                y: 8600,
                y2: 9000,
                borderColor: '#000',
                fillColor: '#FEB019',
                opacity: 0.2,
                label: {
                  borderColor: '#333',
                  style: {
                    fontSize: '10px',
                    color: '#333',
                    background: '#FEB019',
                  },
                  text: 'Y-axis range',
                }
              }],
              xaxis: [{
                x: new Date('23 Nov 2017').getTime(),
                strokeDashArray: 0,
                borderColor: '#775DD0',
                label: {
                  borderColor: '#775DD0',
                  style: {
                    color: '#fff',
                    background: '#775DD0',
                  },
                  text: 'Anno Test',
                }
              }, {
                x: new Date('26 Nov 2017').getTime(),
                x2: new Date('28 Nov 2017').getTime(),
                fillColor: '#B3F7CA',
                opacity: 0.4,
                label: {
                  borderColor: '#B3F7CA',
                  style: {
                    fontSize: '10px',
                    color: '#fff',
                    background: '#00E396',
                  },
                  offsetY: -10,
                  text: 'X-axis range',
                }
              }],
              points: [{
                x: new Date('01 Dec 2017').getTime(),
                y: 8607.55,
                marker: {
                  size: 8,
                  fillColor: '#fff',
                  strokeColor: 'red',
                  radius: 2,
                  cssClass: 'apexcharts-custom-class'
                },
                label: {
                  borderColor: '#FF4560',
                  offsetY: 0,
                  style: {
                    color: '#fff',
                    background: '#FF4560',
                  },

                  text: 'Point Annotation',
                }
              }, {
                x: new Date('08 Dec 2017').getTime(),
                y: 9340.85,
                marker: {
                  size: 0
                },
                image: {
                  path: '../../assets/images/ico-instagram.png'
                }
              }]
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              curve: 'straight'
            },
            grid: {
              padding: {
                right: 30,
                left: 20
              }
            },
            title: {
              text: 'Line with Annotations',
              align: 'left'
            },
            labels: [
                "13 Nov 2017",
                "14 Nov 2017",
                "15 Nov 2017",
                "16 Nov 2017",
                "17 Nov 2017",
                "20 Nov 2017",
                "21 Nov 2017",
                "22 Nov 2017",
                "23 Nov 2017",
                "24 Nov 2017",
                "27 Nov 2017",
                "28 Nov 2017",
                "29 Nov 2017",
                "30 Nov 2017",
                "01 Dec 2017",
                "04 Dec 2017",
                "05 Dec 2017",
                "06 Dec 2017",
                "07 Dec 2017",
                "08 Dec 2017"
            ],
            xaxis: {
              type: 'datetime',
            },
        },
        totalSalesChartOptions: {
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
        totalSalesChartOptions2: {
            chart: {
                height: 160,
                type: 'area',
                sparkline: {
                    enabled: true
                },
            },
            stroke: {
                curve: 'straight'
            },
            fill: {
                opacity: 1,
                gradient: {
                    shade: 'dark',
                    type: "horizontal",
                    shadeIntensity: 0.5,
                    gradientToColors: undefined,
                    inverseColors: true,
                    opacityFrom: 1,
                    opacityTo: 1,
                    stops: [0, 50, 100],
                    colorStops: []
                },
            },
            labels: [...Array(24).keys()].map(n => `2018-09-0${n+1}`),
            yaxis: {
                min: 0
            },
            xaxis: {
                type: 'datetime',
                    labels: {
                        datetimeUTC: false,
                    },
                },
            colors: ['#DCE6EC'],
        },
        totalSalesSeries2: [
            {
                name: 'Sales',
                data: [47, 45, 54, 38, 56, 24, 65, 31, 37, 39, 62, 51, 35, 41, 35, 27, 93, 53, 61, 27, 54, 43, 19, 46]
            }
        ],
        visitTimeChartOptions: {
            chart: {
                height: 350,
                type: 'rangeBar',
                // toolbar: {
                //     show: false,
                // }
            },
            plotOptions: {
                bar: {
                    horizontal: true
                }
            },
            xaxis: {
                type: 'datetime',
                labels: {
                    datetimeUTC: false,
                },
            }
        },
        visitTimeSeries: [
            {
            data: [
            {
            x: '斎藤一',
            y: [
            dayjs('2022-07-01 20:30:00').valueOf(),
            dayjs('2022-07-01 22:51:00').valueOf(),
            ],
            fillColor: '#008FFB'
            },
            {
            x: '斎藤一1',
            y: [
            dayjs('2022-07-01 20:50:00').valueOf(),
            dayjs('2022-07-01 23:51:00').valueOf(),
            ],
            fillColor: '#008FFB'
            },
            {
            x: '斎藤一2',
            y: [
            dayjs('2022-07-01 21:20:00').valueOf(),
            dayjs('2022-07-02 00:15:00').valueOf(),
            ],
            fillColor: '#CAA846'
            },
            {
            x: '斎藤一3',
            y: [
            dayjs('2022-07-02 00:05:00').valueOf(),
            dayjs('2022-07-02 01:30:00').valueOf(),
            ],
            fillColor: '#008FFB'
            },
            {
            x: '斎藤一4',
            y: [
            dayjs('2022-07-01 20:30:00').valueOf(),
            dayjs('2022-07-01 22:51:00').valueOf(),
            ],
            fillColor: '#CAA846'
            },
            {
            x: '斎藤一5',
            y: [
            dayjs('2022-07-01 20:50:00').valueOf(),
            dayjs('2022-07-01 23:51:00').valueOf(),
            ],
            fillColor: '#008FFB'
            },
            ]
            }
        ],
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
        normalVipChartOptions: {
            chart: {
              type: 'pie',
            },
            labels: ['Normal', 'VIP'],
            responsive: [{
              breakpoint: 480,
              options: {
                chart: {
                  width: 200
                },
                legend: {
                  position: 'bottom'
                }
              }
            }]
        },
        appointTypeChartOptions: {
            chart: {
              type: 'pie',
            },
            labels: ['指名', 'フリー'],
            responsive: [{
              breakpoint: 480,
              options: {
                chart: {
                  width: 200
                },
                legend: {
                  position: 'bottom'
                }
              }
            }]
        },
        appointChartOptions: {
            chart: {
              type: 'bar',
              height: 350
            },
            plotOptions: {
              bar: {
                horizontal: false,
                columnWidth: '55%',
                endingShape: 'rounded'
              },
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              show: true,
              width: 2,
              colors: ['transparent']
            },
            xaxis: {
              categories: ['愛理', '華恋', '乙女', '理沙', '美鈴'],
            },
            yaxis: {
              title: {
                text: '￥ (万円)'
              }
            },
            fill: {
              opacity: 1
            },
            tooltip: {
              y: {
                formatter: function (val) {
                  return "$ " + val + " thousands"
                }
              }
            }
        },
        appointSeries: [
            {
                name: '指名料',
                data: [44, 55, 0, 56, 61]
            },
            {
                name: 'ドリンク',
                data: [76, 85, 30, 98, 87]
            },
            {
                name: '同伴料',
                data: [0, 30, 0, 0, 0]
            }
        ],
        productSalesSeries: [
            {
                name: 'Inflation',
                data: [2.3, 3.1, 4.0, 10.1, 4.0, 3.6, 3.2, 2.3, 1.4, 0.8, 0.5, 0.2]
            }
        ],
        productSalesChartOptions: {
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
        currentPage: 1,
        totalRows: 1,
        perPage: 15,
        filter: null,
        filterOn: [],
        fields: [
            {
                key: 'id',
                label: '伝票NO'
            },
            {
                key: 'account_date',
                label: '会計日'
            },
            {
                key: 'customer.customer_no',
                label: '会員No',
            },
            {
                key: 'customer.name',
                label: '顧客名'
            },
            {
                key: 'total_sales',
                label: '総計(税抜)'
            },
            {
                key: 'total_tax_sales',
                label: '総計(税込)'
            },
            {
                key: 'visit_time',
                label: '来店時間'
            },
            {
                key: 'leave_time',
                label: '退店時間'
            },
            {
                key: 'appoint',
                label: '指名'
            },
            {
                key: 'douhan',
                label: '同伴'
            }
        ]
    }),
    components: {
        InputSalesDialog,
    },
    computed: {
        ...mapGetters([
            'sales',
            'salesTopActive'
        ]),
        topActive () {
            if (this.salesTopActive == undefined || this.salesTopActive == 0) {
                return true
            }
            return false
        }
    },
    created () {
    },
    mounted () {
        this.totalRows = this.sales.length
    },
    methods: {
        ...mapMutations([
            'setSalesTopActive'
        ]),
        onRowSelected (item) {
            this.$router.push({
                name: 'SalesDetail',
                params: {
                    id: item[0].id
                }
            })
        }
    }
}
</script>

<style lang="scss" scoped>
    #sales_list_wrap {
        // background-color: $theme-color;
        // background-color: white;
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        height: $main-height;
        padding: 20px;

        .sales_list_area {
            background-color: $theme-color;
            color: white;
        }

        .total_sales_content {
            font-size: 23px;
        }

        .sales_list_area_top {
            height: 430px;
            .sales_list_area_top_left {
                height: 100%;
            }
            .sales_list_area_top_right {
                height: 100%;
                .sales_list_area_top_right1 {
                    height: 50%;
                }
                .sales_list_area_top_right2 {
                    margin-top: 2%;
                    height: 48%;
                }
            }
        }

        .sales_list_area_middle {
            height: 300px;

            .sales_list_area_middle_left {
                height: 100%;
            }
        }
    }
</style>
