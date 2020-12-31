<template>


    <b-container fluid>

        
    <form action="" method="POST" enctype="multipart/form-data" @submit.prevent="submit">

        <b-row>
            
                    <!-- column one  -->
                <div class="col-lg-2 mt-5"> 

                
                    <b-row class="mx-2">
                    
                        <div class="list group">

                            <div class="item-title "> 
                                <h6>

                        <span class="badge badge-pill badge-primary">1</span>  Order details

                                </h6>
                                <p class=" item-description text-muted  ml-4">
                                    Fill in your order requirements.
                                </p>

                            </div>


                        </div>
                        

                    </b-row>

                    <b-row class="mx-2">

                        <div class="list group">

                            <div class="item-title"> 
                                <h6>
                        <span class="badge badge-pill badge-primary">2</span> Instructions
                                </h6>
                                <p class="item-description text-muted ml-4">
                                Leave instructions for your writer
                                </p>

                            </div>


                        </div>
                        

                    </b-row>

                    <b-row class="mx-2">
                        

                        <div class="list group">

                            <div class=" item-title text-left"> 
                                <h6>
                                   <span class="badge badge-pill badge-primary">3</span>  Upload Files
                                </h6>
                                <p class="item-description text-muted mx-4">
                                    Uploads files for assignments and materials
                                </p>

                            </div>


                        </div>
                        

                    </b-row>

                    <hr style=" background-color: #ffff;" class="">

                    <button class="btn btn-primary text-left mb-5 col-12" @click.prevent="Mydelete"> <i class="far fa-trash-alt"></i> Discard draft</button>


                    <div style="position: absolute; bottom: 0px;">
                        
                       <p class="item-description2 .text-muted">
                           You can return to the previous step and change any details if necessary.
                       </p>

                        <!-- <router-link to ="/orderdetails" class="link"><button class="btn  btn-primary text-center col-md-12 "> <i class="fas fa-arrow-left"></i>   Previous  </button></router-link> -->
                        <button class="btn  btn-primary text-center col-md-12 " @click= "back" > <i class="fas fa-arrow-left"></i>   Previous  </button>                         
                    </div>

                </div>
                <!-- column one  -->


                <!-- column two  -->
            <div class="col-lg-8"> 
                    <div class=" ">

                        <h1 class="text-left"><strong>  Order {{ $route.params.id }} <span style="color: #e47c2a"> (Draft) </span> </strong></h1>
                        <div class="ant-card text-left px-3 py-4">
                


                                    <div class="form-group">
                                                
                                        <label for="id_topic"  class="col-form-label">
                                        Assignments topic
                                        </label>

                                        <input v-model="form.topic"  type="text" name="topic" maxlength="255" class=" textInput form-control form-control" id="id_topic" required>

                                    </div>

                                <div class="row ">
                                    

                                    <div class="form-group col-lg-6 col-md-12">
                                                
                                            <label for="id_sources" class="col-form-label ">
                                            Number of Sources
                                            </label>
                                                
                                            <input v-model="form.sources" type="number" name="sources" value="0" class="numberinput form-control form-control" id="id_sources" required>
        
                                    </div>

                                    <div class="form-group col-lg-6 col-md-12">
                                                
                                        <label for="id_style" class="col-form-label ">
                                        Style
                                        </label>

                                        <select v-model="form.style" name="style" class="browser-default custom-select mb-3" required id="id_style" >
                                                <option selected>Style </option>
                                            
                                                <option value="APA">APA</option>
                                            
                                                <option value="MLA">MLA</option>
                                            
                                                <option value="Chicago/Turabian"> Chicago/Turabian</option>

                                                <option value="Harvad">Harvard</option>

                                                <option value="Other">Other</option>

                                                <option value="Not Applicable">Not Applicable</option>
                                            
                                            </select>


                                    </div>

                                </div>

                                <div class="row ">
                                    <div class="form-group col-lg-6 col-md-12">
                                        <label for="id_subject" class="col-form-label ">
                                        Subject
                                        </label>

                                        <select v-model="form.subject" 
                                        name="subject" class="browser-default custom-select mb-3" 
                                        required id="id_service" aria-placeholder="Select subject">
                                                <option selected>-- select subject-- </option>
                                            
                                                <option value="Rewriting">Accounting</option>
                                            
                                                <option value="Editing">Advertising </option>
                                            
                                                <option value="statistics"> Statistics</option>
                                                <option value="Maths"> Maths</option>
                                                <option value="Art"> Art </option>
                                                <option value="Biology"> Biology</option>
                                            
                                            </select>


                                    </div>

                                </div>



                             <div class="form-group ">

                                        <label for="id_instructions" class="col-form-label ">
                                            instructions
                                        </label>
                                                                            
                                        <textarea v-model="form.instructions" type="instructions" name="instructions" rows="4" class=" form-control transparent-input " id="id_instructions" required></textarea>

                             </div>


                                
                           

                        </div>
                        
                    </div>

            </div>

                <!-- column two  -->

                    <!-- column three  -->
                <div class="col-lg-2 mt-5">
                    <div class="ant-card mt-2 mb-5">
                        Order draft
                    </div>

                    <div style="position: absolute; bottom: 0px;">
                        
                        <div class="ant-card mr-2 mt-5 mb-3 text-left px-3 py-4">
                            <h5 class="item-title">Summary: </h5>
                            <div  class="item-description2">
                                <p>Quantity: <span class='text-muted '>  2 page / 550 words</span></p>
                                <p>Deadline:<span class='text-muted'>  08/11/20, 06:04 PM </span></p>
                                <p>Level: <span class='text-muted'> College </span></p>

                            </div>

                        

                         </div>

                        <button type="submit" class="btn btn-primary text-center col-md-12 m"> Next Step <i class="fas fa-arrow-right"></i> </button>
                         
                    </div>



                </div>
                <!-- column three  -->
 
        </b-row>

</form>


    </b-container>
    
</template>

<script>

import router from "@/router"
import axios from 'axios'


export default {
    
    name:"Instructions",
    
    data () {
        return {
            message: "This is a form Component",
            form: {"id":"",
            }
        }
    },

    mounted (){
        axios.get(`http://127.0.0.1:8000/api/instructions/${this.$route.params.id}/`
        ).then( (res) => {
            console.log(res.data)
            this.form = res.data

        }).catch( (e) =>{
            console.log(e)

        })
    },
  
    methods: {
        back () {

            router.push(`/orderdetails/${this.$route.params.id}`)
        },
        submit () {
            console.log(this.form);

            axios.post(`http://127.0.0.1:8000/api/instructions/${this.$route.params.id}/`, {
                body: {"id" : this.$route.params.id ,
                        "form": this.form
                        }
            }) 
            .then((res) => {

                console.log( res.data)
                if (res.data.posted) {
                    router.push("/uploads/" + this.$route.params.id )
                }

            
            })
            .catch((e) => {
                console.log(e)

             })

        },
         Mydelete () {

            axios.delete(`http://127.0.0.1:8000/api/orderdetailsdraft/${this.$route.params.id}/`, {
                body:{"delete": "delete"}
            }) 
            .then((res) => {

                console.log( res.data)
                // var qs = res.data.qs
                console.log(res.data)

                if (res.data.deleted) {

                    router.push("/orderdetails/")
                }

            
            })
            .catch((e) => {
                console.log(e)

             })

            
        }
    }

    
}

</script>

<style scoped>

.item-title {
    font-size: 16px !important;
    text-align: left !important;

}

 .item-description {
    font-size: 14px !important;
    text-align: left !important;
}

.item-description2 {
    font-size: 13px !important;
    text-align: left !important;
}
.item-description2 .text-muted {
    font-size: 12px;
    align-content: center;

}

</style>