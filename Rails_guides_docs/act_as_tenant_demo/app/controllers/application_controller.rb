class ApplicationController < ActionController::Base
  set_current_tenant_by_subdomain_or_domain(:account, :subdomain,:domain)
  before_action do
    binding.irp
  end
end
