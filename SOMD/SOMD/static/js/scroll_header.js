let header = document.querySelector(".header");
let empty = document.querySelector(".EmptyForHeader")
let page = document.querySelector(".somdPage");
let container = document.querySelector(".SDcontainer");

let sidebar = document.querySelector(".sidebar_container");
sidebar.style.display = "none";

let preScroll = page.scrollTop;
let prepreScroll = page.scrollTop;
let nowScroll = page.scrollTop;

let maxScroll = page.scrollHeight - container.clientHeight;

let state = "add";
page.addEventListener('scroll', function(event){
    maxScroll = page.scrollHeight - container.clientHeight;
    // console.log("scroll!");
    nowScroll  = page.scrollTop;
    // header.innerText = maxScroll +" / " +preScroll +" -> "+nowScroll+" = "+(preScroll - nowScroll) + state;
    // console.log(maxScroll)
    // console.log(maxScroll +"/" +preScroll +"->"+nowScroll+"="+(preScroll - nowScroll) + state);
  if(maxScroll > 2){
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
    }
  } 
  prepreScroll = preScroll;
  preScroll = nowScroll;
});
// 
let sidebar_button = document.querySelector(".sidebar_button");

let BlurForSidebar = document.querySelector(".BlurForSidebar");
BlurForSidebar.style.display ="none";
sidebar_button.addEventListener('click', function(event){
  sidebar.style.display = "flex";
  BlurForSidebar.style.display ="block";
});

let sidebar_button_close = document.querySelector(".sidebar_button_close")
sidebar_button_close.addEventListener('click',function(event){
  sidebar.style.display = "none";
  BlurForSidebar.style.display ="none";
});


