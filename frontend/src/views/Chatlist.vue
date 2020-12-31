<template>
  <div id="curtain">
    <v-card class="card" height="100%" light>
      <v-card-title>
        <span class="ml-5">Chats</span>

        <v-spacer></v-spacer>

        <v-btn icon class="mr-5" @click.native="$emit('chatEvent')" light>
          <v-icon>fa-times</v-icon>
        </v-btn>
      </v-card-title>
      <v-divider class="mt-n1"></v-divider>

      <v-card-text class="mt-n5">
        <div id="chat-body">
          <!-- <v-list two-line light dense v-for="(item,index) in items" @click.native="passChat(item.sender); swapComponent('ChatComponent')" :key="index" >
                                <template >

        
                                    <v-list-item 
                                    :key="index"
                                    link>

                                        <v-list-item-avatar>
                                            <v-img src="https://cdn.vuetifyjs.com/images/lists/1.jpg"></v-img>
                                        </v-list-item-avatar>

                                        <v-list-item-content>
                                                <v-list-item-title> Client_{{item.id}} {{item.created_at | dateformat }}</v-list-item-title>

                                                <v-list-item-subtitle v-text="item.text"> </v-list-item-subtitle>
                                        </v-list-item-content>

                                        <v-list-item-icon>
                                                <v-icon color='primary' x-small>mdi-greater-than</v-icon>
                                        </v-list-item-icon>
                                        
                                    </v-list-item>

                                </template>


                            </v-list> -->

          <v-list two-line light dense>
            <v-list-item-group v-model="model">
              <v-list-item
                v-for="(item, i) in items"
                :key="i"
                @click.native="
                  passChat(item.sender);
                  swapComponent('ChatComponent');
                "
              >
                <v-list-item-avatar>
                  <v-img
                    src="https://cdn.vuetifyjs.com/images/lists/1.jpg"
                  ></v-img>
                </v-list-item-avatar>

                <v-list-item-content>
                  <v-list-item-title>
                    Client_{{ item.id }}
                    {{ item.created_at | dateformat }}</v-list-item-title
                  >

                  <v-list-item-subtitle v-text="item.text">
                  </v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-icon>
                  <v-icon color="primary" x-small>mdi-greater-than</v-icon>
                </v-list-item-icon>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

export default {
  name: "Chatlist",
  props: ["swapComponent"],
  data() {
    return {
      message: "2020-09-21T10:36:38.627881Z",
      chatstatus: true,
      items: [
        {
          id: "Ali Connors ",
          created_at: "2020-09-21T10:36:38.627881Z",
          text:
            "i will be in your neighborhood doing errands this weekend. Do you want to hang out?"
        },
        {
          id: "Ali Connors ",
          created_at: ".11h Ago",
          text:
            "I'll be in your neighborhood doing errands this weekend. Do you want to hang out?"
        },
        {
          id: "Ali Connors ",
          created_at: ".11h Ago",
          text:
            "I'll be in your neighborhood doing errands this weekend. Do you want to hang out?"
        },
        {
          id: "Ali Connors ",
          created_at: ".11h Ago",
          text:
            "I'll be in your neighborhood doing errands this weekend. Do you want to hang out?"
        }
      ]
    };
  },

  methods: {
    chatopen() {
      if (this.chatstatus) {
        document.getElementById("curtain").style.display = "none";
      } else {
        document.getElementById("curtain").style.display = "block";
      }
    },
    chatclose() {
      this.chatstatus = !this.chatstatus;
      document.getElementById("curtain").style.display = "none";
    },

    passChat(value) {
      this.$root.$emit("passChat", value);
      console.log("event emitted", value);
    }
  },
  filters: {
    dateformat(value) {
      var date1 = new Date();
      var date2 = moment(date1);
      var date = moment(value).format("YYYY-MM-DD HH:mm");
      const ms = date2.diff(date);
      console.log(date, date, ms);

      var diff = new moment.duration(ms);
      diff.asDays(); // # of days in the duration
      diff.asHours(); // # of hours in the duration
      diff.asMinutes();
      console.log(diff);
      // const miliseconds = diff._data.miliseconds
      const days = diff._data.days;
      const hours = diff._data.hours;
      const minutes = diff._data.minutes;
      var result = "0m Ago";
      if (minutes > 0 && hours < 0) {
        console.log("minutes", minutes);
        result = "." + minutes + "m Ago";
      } else if (minutes > 0 && hours > 0) {
        console.log("hours", hours);
        result = "." + hours + "h Ago";
      } else {
        console.log("days", days);
        result = "." + days + "d Ago";
      }
      return result;
    },

    capitalize: function(value) {
      if (!value) return "";
      value = value.toString();
      return value.charAt(0).toUpperCase() + value.slice(1);
    }
  },
  created() {
    const instance = axios.create({
      baseURL: "http://localhost:8000/",
      headers: { Authorization: "Bearer " + this.$store.state.jwt }
    });

    instance
      .get("/messageAPI/messagelist/")
      .then(res => {
        console.log(res.data.messageslist);
        this.loggedInUser = res.data.current_user;
        this.items = res.data.messageslist;
      })
      .catch(error => {
        console.log(error);
      });
  },

  mounted() {
    this.$root.$on("chatopen", () => {
      this.chatstatus = !this.chatstatus;
      this.chatopen();
      this.value;
    });
  }
};
</script>
<style scoped></style>
