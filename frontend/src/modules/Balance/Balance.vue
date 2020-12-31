<template>
  <v-main class="">
    <h2>My Balance: $0.00</h2>

    <div class="ant-card " style="height:400px;">
      <v-row class="">
        <v-tabs background-color="transparent">
          <v-tab>Trensactions</v-tab>
          <v-tab>Refund requests</v-tab>
          <!-- <v-tab>Closed</v-tab> -->

          <v-tab-item class="mt-3 ">
            <div class="ant-card " style="height:400px;">
              <div class="card-header">
                <h3>Transactions</h3>
              </div>
              <v-data-table
                :headers="headers"
                :items="desserts"
                :items-per-page="5"
                class="elevation-1 mx-5 mb-5"
              ></v-data-table>
            </div>
          </v-tab-item>

          <v-tab-item class="mt-3 ">
            <div class="ant-card " style="height:400px;">
              <div class="card-header">
                <h3>Refund Requests</h3>
              </div>

              <v-data-table
                :headers="Refundheaders"
                :items="RefundItems"
                :items-per-page="5"
                class="elevation-1 mx-5 mb-5"
              ></v-data-table>
            </div>
          </v-tab-item>
        </v-tabs>
      </v-row>
    </div>
  </v-main>
</template>

<script>
export default {
  name: "Balance",
  components: {},
  data() {
    return {
      msg: "hey message",
      headers: [
        { text: "Date", value: "Date" },
        { text: "Type", value: "Type" },
        { text: "Amount", value: "Amount" },
        { text: "Balance", value: "Balance" }
      ],
      desserts: [
        {
          Date: "Frozen Yogurt",
          Type: 159,
          Amount: 6.0,
          Balance: 24
        },
        {
          Date: "Frozen Yogurt",
          Type: 159,
          Amount: 6.0,
          Balance: 24
        },
        {
          Date: "Frozen Yogurt",
          Type: 159,
          Amount: 6.0,
          Balance: 24
        },
        {
          Date: "Frozen Yogurt",
          Type: 159,
          Amount: 6.0,
          Balance: 24
        },
        {
          Date: "Frozen Yogurt",
          Type: 159,
          Amount: 6.0,
          Balance: 24
        },
        {
          Date: "Frozen Yogurt",
          Type: 159,
          Amount: 6.0,
          Balance: 24
        }
      ],

      Refundheaders: [
        { text: "ID", value: "ID" },
        { text: "Requested", value: "Requested" },
        { text: "Paid", value: "Paid" },
        { text: "State", value: "State" },
        { text: "Date", value: "Date" }
      ],
      RefundItems: [
        {
          ID: "233",
          Requested: "$300",
          Paid: "True",
          State: "Paid",
          Date: "07/20/2020"
        }
      ]
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
</style>
