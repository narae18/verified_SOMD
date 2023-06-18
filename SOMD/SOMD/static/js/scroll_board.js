let page_main = document.querySelector(".somdPage");
let page_header = document.querySelector(".somdPage_header");
let somdList = document.querySelector(".somdList");
let all_somdList = document.querySelector(".all_somdList");
let option = document.querySelector(".option");
let Scroll = page_main.scrollTop;
// console.log("연결");

page_main.addEventListener('scroll', function(event){
    Scroll  = page_main.scrollTop;
    // console.log(Scroll);
    if(Scroll>180){
        somdList.style.display = "none";
        page_header.appendChild(option);
    }
    if(Scroll < 3){
        somdList.style.display = "block";
        page_main.insertBefore(option,all_somdList);
    }
    // console.log(option.parentNode);
});
// 


