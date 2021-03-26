# 附录（思考）

## include&extend的使用场景

```ruby

使用include把一个module包含在一个class||module中，使用.ancestors可以发现，include进来的class||module在上面,一般使用include把自己写的module包含进来
eg:

irb(main):001:1* module A
irb(main):002:1*   "this is A"
irb(main):003:0> end
=> "this is A"
irb(main):004:1* class B
irb(main):005:1*   include A
irb(main):006:1*   "this is B"
irb(main):007:0> end
=> "this is B"
irb(main):008:0> B.ancestors
=> [B, A, Object, Kernel, BasicObject]

使用extend,继承其他module，一般使用extend继承ruby自带的module&gem包的module
irb(main):001:1* module A
irb(main):002:1*   "this is A"
irb(main):003:0> end
=> "this is A"
irb(main):004:1* class B
irb(main):005:1*   extend A
irb(main):006:1*   "this is B"
irb(main):007:0> end
=> "this is B"
irb(main):008:0> B.ancestors
=> [B, Object, Kernel, BasicObject]

```



## 动态创建对象&动态调用方法

```ruby
动态创建对象，已知，可以把方法，类看成是对象
所以----
1.动态创建方法----define_method
一般会使用define_method结合method_missing来编写DRY代码！也就是把重复的代码干掉！

2.7.2 :001 > class Developer
2.7.2 :002 >   
2.7.2 :003 >   def coding_frontend
2.7.2 :004 >     p "writing frontend"
2.7.2 :005 >   end
2.7.2 :006 >   
2.7.2 :007 >   def coding_backend
2.7.2 :008 >     p "writing backend"
2.7.2 :009 >   end
2.7.2 :010 >   
2.7.2 :011 > end
 => :coding_backend 
2.7.2 :012 > developer = Developer.new
 => #<Developer:0x00007f9168453d68> 
2.7.2 :013 > developer.coding_frontend
"writing frontend"
 => "writing frontend" 
2.7.2 :014 > developer.coding_backend
"writing backend"
 => "writing backend" 
2.7.2 :015 > class Developer
2.7.2 :016 >   
2.7.2 :017 >   ["frontend", "backend"].each do |method|
2.7.2 :018 >     define_method "coding_#{method}" do
2.7.2 :019 >     p "writing " + method.to_s
2.7.2 :020 >     end
2.7.2 :021 >   end
2.7.2 :022 >   
2.7.2 :023 > end
 => ["frontend", "backend"] 
2.7.2 :024 > developer = Developer.new
 => #<Developer:0x00007f916c9be178> 
2.7.2 :025 > developer.coding_frontend
"writing frontend"
 => "writing frontend" 
2.7.2 :026 > developer.coding_backend
"writing backend"
 => "writing backend"


2.动态创建类----class_eval&instance_eval

动态调用方法，作用是可以消除繁复的代码
and
调用一个方法实际上是给一个对象发送一条消息！

Calling Methods Dynamically

常规的操作是使用点标志符(.)

irb(main):001:1* class MyClass
irb(main):002:2*   def my_method(my_arg)
irb(main):003:2*     my_arg * 2
irb(main):004:1*   end
irb(main):005:0> end
=> :my_method
irb(main):006:0> obj = MyClass.new
irb(main):007:0> obj.my_method(3)
=> 6
irb(main):009:0> obj.send(:my_method,3)
=> 6

在send方法中，想调用的方法变成了参数，可以动态派发！

值得注意的是在动态调用方法中，方法是以Symbol的形式作为参数的，因为Symbol是不可修改的，所以将方法名表示为Symbol，and  String同样也可以作为方法的参数！

last but not least ----

.send甚至可以调用私有方法，假如不想这么做，可以使用.public_send方法！！！

```



## 动态执行脚本

```ruby

# eval
代码执行最直接的方法，也是最直接的方式，就是使用eval
irb(main):009:0> eval("3-1")
=> 2

# instance_eval
将暂时的变化带入对象的上下文中

# class_eval(module_eval)
临时性的进入类定义块的上下文

```

