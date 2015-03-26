<h1 align="center">
<sub>
<img src="http://i.imgur.com/VzoJo7a.png"
      height="331"
      width="732">
</sub>
</h1>
<strong>RiceDB</strong> will be a universal configuration file manager designed to make it easy to obtain configurations for any application that fit your individual needs.

<strong>RiceDB</strong> seeks to follow the <strong>Arch Way</strong>, staying simple, open, and elegant.

Planned features include: CLI configuration preview, github based configuration repositories, a web front end for additional access.

```
package with an installer script                                                                                               
          +                                                                                                                  
          |         +---------------+                                                                                        
          |         |               |                       downloads packages and install                  
          +-------> |   git repos   +--+   <--------------------------------------------------------------------+       
                    |               |  |                                                                        |       
                    +---------------+  |                                                                        |       
                                       v                                                                        +       
                                                                                                       search for candidate  
                              +--------------------------+                                        +-------------------------+
                              |                          |                                        |                         |
                              |       index server       |  +-------------------------------->    |   rice install vim-mlp  |
                              |                          |            index.json                  |                         |
                              +--------------------------+                                        +-------------------------+
                                          ||||
                                          ||||
                              +--------------------------+
                              |      http frontend       |
                              +--------------------------+

              server side                                                                                  client side
```

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/nih0/logos)
