<template>
    <div class="">
                <v-img
                    :src="src"
                    class="my-3"
                    contain
                    height="200"
                    />
                <div class="text-center mx-5">
                    
                    <h3> {{title}} </h3>
                    <P >
                        {{text}}
                    </P>


                </div>
                

    </div>
</template>

<script>
export default {
    name:"PlaceHolder",
    props:[ "src", "title", "text" ],


}
</script>