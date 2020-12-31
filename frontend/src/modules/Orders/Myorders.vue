<template>
  <div class="">
    <v-row class="">
      <v-col>
        <h1 class="float-left">My Orders</h1>
      </v-col>

      <v-col>
        <router-link to="/orderdetails/">
          <v-btn class="primary float-right">
            <v-icon>mdi-plus-circle </v-icon> New Order
          </v-btn>
        </router-link>
      </v-col>
    </v-row>

    <v-row class="">
      <v-tabs background-color="transparent">
        <v-tab>Opened</v-tab>
        <v-tab>Draft</v-tab>
        <v-tab>Closed</v-tab>

        <v-tab-item class="mt-3 ">
          <div class="ant-card  " style="height:400px;">
            <div class="card-header">
              <h3>Opened Orders</h3>
            </div>

            <PlaceHolder
              style="width:70vw"
              v-if="true"
              :src="require('@/assets/img/svg/no-notifications.svg')"
              title=" Nothing Here"
              text=" Your opened orders appears here when you create first order"
            />

            <OpenedOrder
              v-else
              :topic="propsorder.topic"
              :pages="propsorder.pages"
              :type="propsorder.type"
              :language="propsorder.language"
              :status="propsorder.status"
              :amount="propsorder.amount"
              :time="propsorder.time"
            />
          </div>
        </v-tab-item>

        <v-tab-item class="mt-3 ">
          <div class="ant-card " style="height:400px;">
            <div class="card-header">
              <h3>Draft orders</h3>
            </div>
            <orderlist
              :topic="propsorder.topic"
              :pages="propsorder.pages"
              :type="propsorder.type"
              :language="propsorder.language"
              :status="propsorder.status"
              :amount="propsorder.amount"
              :time="propsorder.time"
            />
          </div>
        </v-tab-item>

        <v-tab-item class="mt- ">
          <div class="ant-card " style="height:400px;">
            <div class="card-header">
              <h3 class="float-left">Orders Closed</h3>
            </div>

            <ClosedOrder
              :topic="propsorder.topic"
              :pages="propsorder.pages"
              :type="propsorder.type"
              :language="propsorder.language"
              :status="propsorder.status"
              :amount="propsorder.amount"
              :time="propsorder.time"
            />
          </div>
        </v-tab-item>
      </v-tabs>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "Myorders",
  components: {
    Orderlist: () => import("@/modules/Orders/order_list"),
    ClosedOrder: () => import("@/modules/Orders/ClosedOrder"),
    OpenedOrder: () => import("@/modules/Orders/OpenedOrder"),
    PlaceHolder: () => import("@/components/core/PlaceHolder")
  },
  data() {
    return {
      msg: "hey message",
      propsorder: {
        topic: "Python",
        pages: "2",
        type: "Essay (any)",
        language: "English (UK)",
        status: "Draft",
        amount: "7",
        time: "2 days remaining"
      }
    };
  }
};
</script>

<style scoped>
.card-header {
  background: #232c3b;
  height: 70px;
  border: 2px solid #273142;
  border-radius: 4px;
}

.icon {
  width: 70px;
  text-align: left;
}
.Field {
  width: 100%;
  text-align: left;
  font-size: 20px;
  font-weight: 500;
  border: 2px solid #a2a3a5;
  border-radius: 4px;
}

.inputContainer i {
  position: absolute;
}
</style>
