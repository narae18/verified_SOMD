let header = document.querySelector(".header");
let empty = document.querySelector(".EmptyForHeader")
let page = document.querySelector(".somdPage");
let container = document.querySelector(".SDcontainer");
let preScroll = page.scrollTop;
let prepreScroll = page.scrollTop;
let nowScroll = page.scrollTop;

let maxScroll = page.scrollHeight - page.clientHeight;

let state = "add";
page.addEventListener('scroll', function(event){
    maxScroll = page.scrollHeight - page.clientHeight;
    // console.log("scroll!");
    nowScroll  = page.scrollTop;
    // header.innerText = maxScroll +" / " +preScroll +" -> "+nowScroll+" = "+(preScroll - nowScroll) + state;
    // console.log(maxScroll)
    // console.log(maxScroll +"/" +preScroll +"->"+nowScroll+"="+(preScroll - nowScroll) + state);
  
  if(prepreScroll != nowScroll){
    if(nowScroll <-1){
        // console.log("add");
        header.classList.add("add");
        header.classList.remove("remove");
        state = "top";
        empty.classList.add("addEmpty");
        empty.classList.remove("removeEmpty");
     
      }
    
      else if(nowScroll > maxScroll+1){
        header.classList.remove("add");
        header.classList.add("remove");
        state = "bottom";
        empty.classList.remove("addEmpty");
        empty.classList.add("removeEmpty");
     
      }
      else{
        if (preScroll - nowScroll > 5 &&(( state !="bottom")||(nowScroll <= maxScroll && state == "bottom")) ){
            // console.log("add");
            header.classList.add("add");
            header.classList.remove("remove");
            state = "add";
            empty.classList.add("addEmpty");
            empty.classList.remove("removeEmpty");
          } 
        
          else if(preScroll - nowScroll < -5 && ((state !="top")  || (nowScroll >= 0 && state == "top"))) {
            // console.log("remove");
            header.classList.remove("add");
            header.classList.add("remove");
            state = "remove";
            empty.classList.remove("addEmpty");
            empty.classList.add("removeEmpty");
          }
      }
      if(page.scrollHeight - page.clientHeight == 0){
        header.classList.add("add");
        header.classList.remove("remove");
        state = "add";
        empty.classList.add("addEmpty");
        empty.classList.remove("removeEmpty");
    }
  } 
  prepreScroll = preScroll;
  preScroll = nowScroll;
});
// 


