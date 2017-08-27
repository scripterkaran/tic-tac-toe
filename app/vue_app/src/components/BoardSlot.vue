<template>
  <div class="slot-box" @click="markMove">
    <span> {{text}}</span></div>
</template>

<script>
  export default {
      props: ['user_selection'],
      data(){
          return{
              text: ''
          }
      },
      methods:{
        markMove(){
            this.text = this.user_selection
        }
      }
  }
</script>

<style scoped>
  .slot-box{
    border: 1px solid red;
    min-height: 40px;
    min-width: 40px;
  }
  .slot-box span {
    text-transform: uppercase;
    font-size: 18px;
    font-weight: 600;
    text-align: center;
    line-height: 40px;
  }
</style>
