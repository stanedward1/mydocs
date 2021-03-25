# 附录（思考）

- ## instance methods & class methods

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

- ## scope&unscope&unscoped

- ## .constantize