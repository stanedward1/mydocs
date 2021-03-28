<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [附录（思考）](#%E9%99%84%E5%BD%95%E6%80%9D%E8%80%83)
  - [instance methods & class methods](#instance-methods--class-methods)
  - [scope&unscope&unscoped](#scopeunscopeunscoped)
  - [.constantize](#constantize)
  - [*args&**args](#argsargs)
  - [super keyword](#super-keyword)
  - [ruby中的简写](#ruby%E4%B8%AD%E7%9A%84%E7%AE%80%E5%86%99)
  - [：：](#)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 附录（思考）

## instance methods & class methods

```ruby
irb(main):001:1* class Developer
irb(main):002:2*   def frontend
irb(main):003:2*     self
irb(main):004:1*   end
irb(main):005:0> end
=> :frontend
irb(main):006:0> Developer.new.frontend
=> #<Developer:0x000055de97468c48>
```

```ruby
irb(main):007:1* class Developer
irb(main):008:2*   def self.backend
irb(main):009:2*     self
irb(main):010:1*   end
irb(main):011:0> end
=> :backend
irb(main):012:0> Developer.backend
=> Developer
```

## scope&unscope&unscoped

字面意思：作用域，取消作用，全部取消作用

那么，下一步来看看例子！！

```ruby
class Book < ApplicationRecord
  scope :out_of_print, -> { where(out_of_print: true) }
end
```

等价于

```ruby
class Book < ApplicationRecord
    def self.out_of_print
        where(out_of_print: true)}
	end
end
```

```ruby
Book.where('id > 100').limit(20).order('id desc').unscope(:order)
```

```sql
SELECT * FROM books WHERE id > 100 LIMIT 20
```

关于unscope，有个gem包，叫做——acts_as_tenant,使用这个gem包时，需要在model层中进行注册，然后default_scope起作用，一个系统内的一个用户就无法获取另外一个用户的数据了，假如想要获取其他人的数据，这时候unscoped就起作用了！

举个栗子！！！栗子！！！

```ruby
Article.unscoped.create(account_id:self.id)
```

## .constantize

主要作用是把一个字符串创建为一个对象，比如说一个类

## *args&**args

本来以为类似_x,$x,@x,@@x互相的关系,四者分别是局部变量，全局变量，实例变量，类变量
但是理解的不太对，也不太深入
整理一下叭！！！
本质是参数！
*args:Use Variable Arguments to Capture as Many Values as Necessary(使用可变参数来获得尽可能多的值，)

```
irb(main):085:1* def print_all(*args)
irb(main):086:1*   "this is *args"
irb(main):087:0> end
=> :print_all
irb(main):088:0> print_all(1,2,3,4)
=> "this is *args"
```

*args可以与其他类型参数结合使用

**Here’s the valid order of arguments** 
**if you want to combine them & avoid a syntax error:**

**---->required -> optional -> variable -> keyword**

```shell
irb(main):098:1* def testing(a, b = 1, *c, d: 1, **x)
irb(main):099:1*   p a,b,c,d,x
irb(main):100:0> end
=> :testing
irb(main):101:0> 
irb(main):102:0> testing('a', 'b', 'c', 'd', 'e', d: 2, x: 1)
"a"
"b"
["c", "d", "e"]
2
{:x=>1}
=> ["a", "b", ["c", "d", "e"], 2, {:x=>1}]
```

*args返回一个数组，**args返回一个为hash

```ruby
# 该方法接受任何参数，但不对他们做任何事情
def print_all(*)
end
```

```shell
# 通常和super一起用
# 当Food类的nutrition方法更改参数时，不必更改Bacon的参数

irb(main):103:1* class Food
irb(main):104:2*   def nutrition(vitamins, minerals)
irb(main):105:2*     puts vitamins
irb(main):106:2*     puts minerals
irb(main):107:1*   end
irb(main):108:0> end
=> :nutrition
irb(main):109:1* class Bacon < Food
irb(main):110:2*   def nutrition(*)
irb(main):111:2*     super
irb(main):112:1*   end
irb(main):113:0> end
=> :nutrition
irb(main):114:0> bacon = Bacon.new
irb(main):115:0> bacon.nutrition("b6","Iron")
b6
Iron
=> nil
```

使用可选参数可以增加灵活性！

## super keyword

上一个例子里出现了super关键字，正好一起整理以下！

```ruby
class Food
  def nutrition(vitamins, minerals)
    puts vitamins
    puts minerals
  end
end

class Bacon < Food
  def nutrition(*)
    super
  end
end

bacon = Bacon.new

bacon.nutrition("B6", "Iron")

# 对比代码来看，调用nutrition方法时，super在该方法内调用，and，RUby将尝试去拥有该方法的父类上去调用该方法。
irb(main):020:0> Bacon.ancestors
=> [Bacon, Food, Object, Kernel, BasicObject]
那么，super会去调用Food类里的nutrition方法。

方法不存在时候会触发异常
irb(main):021:0> bacon.nutritions("B6", "Iron")
Traceback (most recent call last):
        4: from /usr/bin/irb:23:in `<main>'
        3: from /usr/bin/irb:23:in `load'
        2: from /usr/lib/ruby/gems/2.7.0/gems/irb-1.2.1/exe/irb:11:in `<top (required)>'
        1: from (irb):21
NoMethodError (undefined method `nutritions' for #<Bacon:0x0000560f6814a7f8>)

结合幽灵方法——method_missing试试

irb(main):068:1* class Animal
irb(main):069:2*   def method_missing(m,*args,&block)
irb(main):070:3*     if m.to_s == "fly"
irb(main):071:3*       "Sorry, dogs can't fly"
irb(main):072:3*     else
irb(main):073:3*       super
irb(main):074:2*     end
irb(main):075:1*   end
irb(main):076:2*   def walk
irb(main):077:2*     "Walking"
irb(main):078:1*   end
irb(main):079:0> end
=> :walk
irb(main):063:0> dog = Animal.new
irb(main):064:0> dog.walk
=> "I am walking"
irb(main):065:0> dog.fly
=> "Sorry, dogs can't fly"

last but not least
super()的作用是：super找到父类的方法时，可能传的参数数量对不上，这时候就可以使用super()
```

## ruby中的简写

1. 方法调用的最外层括号可以省略
2. 函数最后一行默认有return
3. hash最外面的{}在大多数情况下可以省略
4. 调用block，就是proc里说的&:
5. module不能被new，可以被include
6. do end as same as {}

## ：：

这个：：可以去拿方法内的常量

and

去操作类方法