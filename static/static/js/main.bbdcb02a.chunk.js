(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{100:function(e,t,n){},217:function(e,t,n){"use strict";n.r(t);n(91);var r=n(62),a=n.n(r),o={};!function(){var e=document.getElementById("client-data"),t=e&&e.innerHTML||"{}";try{Object.assign(o,JSON.parse(t)),a()("articulator:client-data:success")("load",o)}catch(n){a()("articulator:client-data:error")("load",n)}}();var c=n(1),i=n.n(c),s=n(27),u=n(35),l=n(29),d=n(40),p=n(21),f=n.n(p),m=(n(116),n(18)),h=n(93),E=n.n(h),b=n(97),O=n(19),j="GET_USER",v="GET_USER_SUCCESS",S="GET_USER_FAILURE",g=n(33),y=n(34),_=n(94),w=n.n(_),C=new(function(){function e(){Object(g.a)(this,e),this.instance=w.a.create({baseURL:"".concat(window.location.origin,"/api/v1/accounts/"),withCredentials:!0})}return Object(y.a)(e,[{key:"generateFetchOptions",value:function(e,t,n){var r=btoa("test:test"),a={method:e,credentials:"same-origin",headers:{"Content-Type":"application/json",Authorization:"Token ".concat(r),"X-Requested-With":"XMLHttpRequest",Accept:"application/json"}};return"POST"!==e&&"PUT"!==e||(t instanceof FormData?a.body=t:(a.body=JSON.stringify(t),a.headers["Content-Type"]="application/json")),a}},{key:"delete",value:function(e){return this.instance.delete(e)}},{key:"getData",value:function(e){return this.instance.get(e)}},{key:"postData",value:function(e,t){return fetch("".concat(window.location.origin,"/api/v1/accounts/").concat(e),this.generateFetchOptions("POST",t,o._csrf)).then(function(e){return e.ok?new Promise(function(t){return e.json().then(function(e){t({data:e})})}):Promise.reject(e)})}},{key:"putData",value:function(e,t){return fetch("".concat(window.location.origin,"/api/v1/accounts/").concat(e),this.generateFetchOptions("PUT",t,o._csrf)).then(function(e){return e.ok?new Promise(function(t){return e.json().then(function(e){t({data:e})})}):Promise.reject(e)})}}]),e}()),k=f.a.mark(T);function T(e){var t,n;return f.a.wrap(function(r){for(;;)switch(r.prev=r.next){case 0:return r.prev=0,"accounts/login",t=e.postData,r.next=5,Object(O.b)([C,C.postData],"accounts/login",t);case 5:if(0!==(n=r.sent).data.code){r.next=11;break}return r.next=9,Object(O.d)({type:v,error:n.data.err});case 9:r.next=13;break;case 11:return r.next=13,Object(O.d)({type:S,error:n.data.err||"Internal server error."});case 13:r.next=19;break;case 15:return r.prev=15,r.t0=r.catch(0),r.next=19,Object(O.d)({type:S,error:"Failed to connect the server!"});case 19:case"end":return r.stop()}},k,null,[[0,15]])}var P=f.a.mark(U);function U(){return f.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Object(O.e)(j,T);case 2:case"end":return e.stop()}},P)}var D=n(7),A=Object(m.c)({login:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=arguments.length>1?arguments[1]:void 0;switch(t.type){case j:return Object(D.a)({},e,{stage:2,loading:!0,error:"",displayClass:"show"});case v:return Object(D.a)({},e,{stage:3,error:t.error,loading:!1,displayClass:"hide"});case S:return Object(D.a)({},e,{stage:4,loading:!1,error:t.error,displayClass:"hide"});default:return e}},feedback:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=arguments.length>1?arguments[1]:void 0;switch(t.type){case"POST_FEEDBACK":return Object(D.a)({},e,{err:""});case"POST_FEEDBACK_SUCCESS":return Object(D.a)({},e,{err:t.err});case"POST_FEEDBACK_FAILURE":return Object(D.a)({},e,{err:t.err||"Failed to send feedback!"});default:return e}},accessRequest:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=arguments.length>1?arguments[1]:void 0;switch(t.type){case"SEND_ACCESS_REQUEST":return Object(D.a)({},e,{err:""});case"SEND_ACCESS_REQUEST_SUCCESS":return Object(D.a)({},e,{err:t.err});case"SEND_ACCESS_REQUEST_FAILURE":return Object(D.a)({},e,{err:t.err||"Failed to send Request!"});default:return e}},ldapSearch:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=arguments.length>1?arguments[1]:void 0;switch(t.type){case"LDAP_SEARCH":return Object(D.a)({},e,{info:""});case"LDAP_SEARCH_SUCCESS":return Object(D.a)({},e,{info:t.info});case"LDAP_SEARCH_FAILURE":return Object(D.a)({},e,{info:t.info||"LDAP search failed!"});default:return e}}}),R=f.a.mark(M),x=window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__?window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__:m.d;function M(){return f.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Object(O.a)([Object(O.c)(U)]);case 2:case"end":return e.stop()}},R)}var F=Object(b.a)(),I=[E.a,F],L=Object(m.e)(A,x(m.a.apply(void 0,I)));F.run(M);var N=n(20),B=n(64),H=n.n(B),X=n(42),q=n.n(X),G=n(51),J=n(50),K=n(52),Q=function(e){function t(e){return Object(g.a)(this,t),Object(G.a)(this,Object(J.a)(t).call(this,e))}return Object(K.a)(t,e),Object(y.a)(t,[{key:"componentWillMount",value:function(){console.log(111),this.props.loginUser({})}},{key:"render",value:function(){this.props.classes;return i.a.createElement("div",{id:"home"},"login")}}]),t}(i.a.Component);Q.defaultProps={};var W=Object(u.b)(function(e){return{}},{loginUser:function(e){return{type:j,postData:e,displayClass:"show"}}})(Q),V=Object(N.withStyles)(function(e){return{}},{withTheme:!0})(W),z=n(96),Y=n.n(z),Z=function(e){return i.a.createElement(d.b,Object.assign({to:"/login"},e))},$=function(e){function t(e){return Object(g.a)(this,t),Object(G.a)(this,Object(J.a)(t).call(this,e))}return Object(K.a)(t,e),Object(y.a)(t,[{key:"componentWillMount",value:function(){console.log(1111)}},{key:"render",value:function(){this.props.classes;return i.a.createElement("div",{id:"home"},"home",i.a.createElement("div",null,i.a.createElement(Y.a,{variant:"contained",color:"primary",component:Z},"Get Started")))}}]),t}(i.a.Component);$.defaultProps={};var ee=Object(u.b)(function(e){return{}})($),te=Object(N.withStyles)(function(e){return{}},{withTheme:!0})(ee),ne=function(){return i.a.createElement(l.a,{from:"*",to:"/"})},re=function(){return i.a.createElement(l.d,null,i.a.createElement(l.b,{exact:!0,path:"/",component:te}),i.a.createElement(l.b,{render:ne}))},ae=function(){return i.a.createElement(l.d,null,i.a.createElement(l.b,{path:"/login",component:V}))},oe=n(61),ce=n.n(oe),ie=n(60),se="#9966ff",ue=n.n(ie)()({primary:{main:se}}),le={typography:{fontFamily:["PayPal-Sans","-apple-system","BlinkMacSystemFont",'"Segoe UI"',"Roboto",'"Helvetica Neue"',"Arial","sans-serif",'"Apple Color Emoji"','"Segoe UI Emoji"','"Segoe UI Symbol"'].join(",")},overrides:{MuiPaper:{root:{padding:20}},MuiTooltip:{tooltip:{backgroundColor:se}},MuiIcon:{root:{width:24,height:24}},MuiIconButton:{root:{width:40,height:40}},MuiAvatar:{colorDefault:{color:"black",backgroundColor:ce.a[200]}},MuiMenuItem:{root:{color:ue.text.primary},selected:{backgroundColor:"transparent !important",color:ue.secondary.main}}},palette:ue},de=Object(D.a)({},le,{overrides:Object(D.a)({},le.overrides,{MuiPaper:{root:{padding:"20px",marginBottom:"20px"}}}),palette:Object(D.a)({},le.palette,{primary:Object(D.a)({},le.palette.primary,{main:"#9966ff"})})}),pe=Object(N.createMuiTheme)(de),fe=L;Object(s.render)(i.a.createElement(u.a,{store:fe},i.a.createElement(d.a,{basename:o.requestURI},i.a.createElement(l.d,null,i.a.createElement(l.b,{exact:!0,path:"/login",component:function(){return i.a.createElement(N.MuiThemeProvider,{theme:pe},i.a.createElement(H.a,null),i.a.createElement(q.a,{container:!0,justify:"center"},i.a.createElement(q.a,{item:!0,xs:10},i.a.createElement(ae,null))))}}),i.a.createElement(l.b,{path:"/",component:function(){return i.a.createElement(N.MuiThemeProvider,{theme:pe},i.a.createElement(H.a,null),i.a.createElement(q.a,{container:!0,justify:"center"},i.a.createElement(q.a,{item:!0,xs:10},i.a.createElement(re,null))))}})))),document.getElementById("root"))},98:function(e,t,n){e.exports=n(99)},99:function(e,t,n){"use strict";n.r(t);n(100);document.addEventListener("DOMContentLoaded",function(){n(217)})}},[[98,1,2]]]);
//# sourceMappingURL=main.bbdcb02a.chunk.js.map