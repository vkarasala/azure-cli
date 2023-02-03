# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "vmss nic show",
)
class Show(AAZCommand):
    """Get the specified network interface in a virtual machine scale set.
    """

    _aaz_info = {
        "version": "2016-03-30",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/virtualmachinescalesets/{}/virtualmachines/{}/networkinterfaces/{}", "2016-03-30"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.network_interface_name = AAZStrArg(
            options=["-n", "--name", "--network-interface-name"],
            help="The network interface (NIC).",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.",
            required=True,
        )
        _args_schema.virtual_machine_scale_set_name = AAZStrArg(
            options=["--vmss-name", "--virtual-machine-scale-set-name"],
            help="Scale set name.",
            required=True,
            id_part="name",
        )
        _args_schema.virtualmachine_index = AAZStrArg(
            options=["--instance-id", "--virtualmachine-index"],
            help="The virtual machine index.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="Expands referenced resources. Default value is None.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NetworkInterfacesGetVirtualMachineScaleSetNetworkInterface(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NetworkInterfacesGetVirtualMachineScaleSetNetworkInterface(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines/{virtualmachineIndex}/networkInterfaces/{networkInterfaceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "networkInterfaceName", self.ctx.args.network_interface_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualMachineScaleSetName", self.ctx.args.virtual_machine_scale_set_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualmachineIndex", self.ctx.args.virtualmachine_index,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$expand", self.ctx.args.expand,
                ),
                **self.serialize_query_param(
                    "api-version", "2016-03-30",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _ShowHelper._build_schema_network_interface_read(cls._schema_on_200)

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_ip_configuration_read = None

    @classmethod
    def _build_schema_ip_configuration_read(cls, _schema):
        if cls._schema_ip_configuration_read is not None:
            _schema.etag = cls._schema_ip_configuration_read.etag
            _schema.id = cls._schema_ip_configuration_read.id
            _schema.name = cls._schema_ip_configuration_read.name
            _schema.properties = cls._schema_ip_configuration_read.properties
            return

        cls._schema_ip_configuration_read = _schema_ip_configuration_read = AAZObjectType()

        ip_configuration_read = _schema_ip_configuration_read
        ip_configuration_read.etag = AAZStrType()
        ip_configuration_read.id = AAZStrType()
        ip_configuration_read.name = AAZStrType()
        ip_configuration_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_ip_configuration_read.properties
        properties.private_ip_address = AAZStrType(
            serialized_name="privateIPAddress",
        )
        properties.private_ip_allocation_method = AAZStrType(
            serialized_name="privateIPAllocationMethod",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.public_ip_address = AAZObjectType(
            serialized_name="publicIPAddress",
        )
        cls._build_schema_public_ip_address_read(properties.public_ip_address)
        properties.subnet = AAZObjectType()
        cls._build_schema_subnet_read(properties.subnet)

        _schema.etag = cls._schema_ip_configuration_read.etag
        _schema.id = cls._schema_ip_configuration_read.id
        _schema.name = cls._schema_ip_configuration_read.name
        _schema.properties = cls._schema_ip_configuration_read.properties

    _schema_network_interface_ip_configuration_read = None

    @classmethod
    def _build_schema_network_interface_ip_configuration_read(cls, _schema):
        if cls._schema_network_interface_ip_configuration_read is not None:
            _schema.etag = cls._schema_network_interface_ip_configuration_read.etag
            _schema.id = cls._schema_network_interface_ip_configuration_read.id
            _schema.name = cls._schema_network_interface_ip_configuration_read.name
            _schema.properties = cls._schema_network_interface_ip_configuration_read.properties
            return

        cls._schema_network_interface_ip_configuration_read = _schema_network_interface_ip_configuration_read = AAZObjectType()

        network_interface_ip_configuration_read = _schema_network_interface_ip_configuration_read
        network_interface_ip_configuration_read.etag = AAZStrType()
        network_interface_ip_configuration_read.id = AAZStrType()
        network_interface_ip_configuration_read.name = AAZStrType()
        network_interface_ip_configuration_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_network_interface_ip_configuration_read.properties
        properties.application_gateway_backend_address_pools = AAZListType(
            serialized_name="applicationGatewayBackendAddressPools",
        )
        properties.load_balancer_backend_address_pools = AAZListType(
            serialized_name="loadBalancerBackendAddressPools",
        )
        properties.load_balancer_inbound_nat_rules = AAZListType(
            serialized_name="loadBalancerInboundNatRules",
        )
        properties.primary = AAZBoolType()
        properties.private_ip_address = AAZStrType(
            serialized_name="privateIPAddress",
        )
        properties.private_ip_address_version = AAZStrType(
            serialized_name="privateIPAddressVersion",
        )
        properties.private_ip_allocation_method = AAZStrType(
            serialized_name="privateIPAllocationMethod",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.public_ip_address = AAZObjectType(
            serialized_name="publicIPAddress",
        )
        cls._build_schema_public_ip_address_read(properties.public_ip_address)
        properties.subnet = AAZObjectType()
        cls._build_schema_subnet_read(properties.subnet)

        application_gateway_backend_address_pools = _schema_network_interface_ip_configuration_read.properties.application_gateway_backend_address_pools
        application_gateway_backend_address_pools.Element = AAZObjectType()

        _element = _schema_network_interface_ip_configuration_read.properties.application_gateway_backend_address_pools.Element
        _element.etag = AAZStrType()
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_network_interface_ip_configuration_read.properties.application_gateway_backend_address_pools.Element.properties
        properties.backend_addresses = AAZListType(
            serialized_name="backendAddresses",
        )
        properties.backend_ip_configurations = AAZListType(
            serialized_name="backendIPConfigurations",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )

        backend_addresses = _schema_network_interface_ip_configuration_read.properties.application_gateway_backend_address_pools.Element.properties.backend_addresses
        backend_addresses.Element = AAZObjectType()

        _element = _schema_network_interface_ip_configuration_read.properties.application_gateway_backend_address_pools.Element.properties.backend_addresses.Element
        _element.fqdn = AAZStrType()
        _element.ip_address = AAZStrType(
            serialized_name="ipAddress",
        )

        backend_ip_configurations = _schema_network_interface_ip_configuration_read.properties.application_gateway_backend_address_pools.Element.properties.backend_ip_configurations
        backend_ip_configurations.Element = AAZObjectType()
        cls._build_schema_network_interface_ip_configuration_read(backend_ip_configurations.Element)

        load_balancer_backend_address_pools = _schema_network_interface_ip_configuration_read.properties.load_balancer_backend_address_pools
        load_balancer_backend_address_pools.Element = AAZObjectType()

        _element = _schema_network_interface_ip_configuration_read.properties.load_balancer_backend_address_pools.Element
        _element.etag = AAZStrType()
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_network_interface_ip_configuration_read.properties.load_balancer_backend_address_pools.Element.properties
        properties.backend_ip_configurations = AAZListType(
            serialized_name="backendIPConfigurations",
        )
        properties.load_balancing_rules = AAZListType(
            serialized_name="loadBalancingRules",
        )
        properties.outbound_nat_rule = AAZObjectType(
            serialized_name="outboundNatRule",
        )
        cls._build_schema_sub_resource_read(properties.outbound_nat_rule)
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )

        backend_ip_configurations = _schema_network_interface_ip_configuration_read.properties.load_balancer_backend_address_pools.Element.properties.backend_ip_configurations
        backend_ip_configurations.Element = AAZObjectType()
        cls._build_schema_network_interface_ip_configuration_read(backend_ip_configurations.Element)

        load_balancing_rules = _schema_network_interface_ip_configuration_read.properties.load_balancer_backend_address_pools.Element.properties.load_balancing_rules
        load_balancing_rules.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(load_balancing_rules.Element)

        load_balancer_inbound_nat_rules = _schema_network_interface_ip_configuration_read.properties.load_balancer_inbound_nat_rules
        load_balancer_inbound_nat_rules.Element = AAZObjectType()

        _element = _schema_network_interface_ip_configuration_read.properties.load_balancer_inbound_nat_rules.Element
        _element.etag = AAZStrType()
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_network_interface_ip_configuration_read.properties.load_balancer_inbound_nat_rules.Element.properties
        properties.backend_ip_configuration = AAZObjectType(
            serialized_name="backendIPConfiguration",
        )
        cls._build_schema_network_interface_ip_configuration_read(properties.backend_ip_configuration)
        properties.backend_port = AAZIntType(
            serialized_name="backendPort",
        )
        properties.enable_floating_ip = AAZBoolType(
            serialized_name="enableFloatingIP",
        )
        properties.frontend_ip_configuration = AAZObjectType(
            serialized_name="frontendIPConfiguration",
        )
        cls._build_schema_sub_resource_read(properties.frontend_ip_configuration)
        properties.frontend_port = AAZIntType(
            serialized_name="frontendPort",
        )
        properties.idle_timeout_in_minutes = AAZIntType(
            serialized_name="idleTimeoutInMinutes",
        )
        properties.protocol = AAZStrType()
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )

        _schema.etag = cls._schema_network_interface_ip_configuration_read.etag
        _schema.id = cls._schema_network_interface_ip_configuration_read.id
        _schema.name = cls._schema_network_interface_ip_configuration_read.name
        _schema.properties = cls._schema_network_interface_ip_configuration_read.properties

    _schema_network_interface_read = None

    @classmethod
    def _build_schema_network_interface_read(cls, _schema):
        if cls._schema_network_interface_read is not None:
            _schema.etag = cls._schema_network_interface_read.etag
            _schema.id = cls._schema_network_interface_read.id
            _schema.location = cls._schema_network_interface_read.location
            _schema.name = cls._schema_network_interface_read.name
            _schema.properties = cls._schema_network_interface_read.properties
            _schema.tags = cls._schema_network_interface_read.tags
            _schema.type = cls._schema_network_interface_read.type
            return

        cls._schema_network_interface_read = _schema_network_interface_read = AAZObjectType()

        network_interface_read = _schema_network_interface_read
        network_interface_read.etag = AAZStrType()
        network_interface_read.id = AAZStrType()
        network_interface_read.location = AAZStrType()
        network_interface_read.name = AAZStrType(
            flags={"read_only": True},
        )
        network_interface_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        network_interface_read.tags = AAZDictType()
        network_interface_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_network_interface_read.properties
        properties.dns_settings = AAZObjectType(
            serialized_name="dnsSettings",
        )
        properties.enable_ip_forwarding = AAZBoolType(
            serialized_name="enableIPForwarding",
        )
        properties.ip_configurations = AAZListType(
            serialized_name="ipConfigurations",
        )
        properties.mac_address = AAZStrType(
            serialized_name="macAddress",
        )
        properties.network_security_group = AAZObjectType(
            serialized_name="networkSecurityGroup",
        )
        cls._build_schema_network_security_group_read(properties.network_security_group)
        properties.primary = AAZBoolType()
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.resource_guid = AAZStrType(
            serialized_name="resourceGuid",
        )
        properties.virtual_machine = AAZObjectType(
            serialized_name="virtualMachine",
        )
        cls._build_schema_sub_resource_read(properties.virtual_machine)

        dns_settings = _schema_network_interface_read.properties.dns_settings
        dns_settings.applied_dns_servers = AAZListType(
            serialized_name="appliedDnsServers",
        )
        dns_settings.dns_servers = AAZListType(
            serialized_name="dnsServers",
        )
        dns_settings.internal_dns_name_label = AAZStrType(
            serialized_name="internalDnsNameLabel",
        )
        dns_settings.internal_domain_name_suffix = AAZStrType(
            serialized_name="internalDomainNameSuffix",
        )
        dns_settings.internal_fqdn = AAZStrType(
            serialized_name="internalFqdn",
        )

        applied_dns_servers = _schema_network_interface_read.properties.dns_settings.applied_dns_servers
        applied_dns_servers.Element = AAZStrType()

        dns_servers = _schema_network_interface_read.properties.dns_settings.dns_servers
        dns_servers.Element = AAZStrType()

        ip_configurations = _schema_network_interface_read.properties.ip_configurations
        ip_configurations.Element = AAZObjectType()
        cls._build_schema_network_interface_ip_configuration_read(ip_configurations.Element)

        tags = _schema_network_interface_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_network_interface_read.etag
        _schema.id = cls._schema_network_interface_read.id
        _schema.location = cls._schema_network_interface_read.location
        _schema.name = cls._schema_network_interface_read.name
        _schema.properties = cls._schema_network_interface_read.properties
        _schema.tags = cls._schema_network_interface_read.tags
        _schema.type = cls._schema_network_interface_read.type

    _schema_network_security_group_read = None

    @classmethod
    def _build_schema_network_security_group_read(cls, _schema):
        if cls._schema_network_security_group_read is not None:
            _schema.etag = cls._schema_network_security_group_read.etag
            _schema.id = cls._schema_network_security_group_read.id
            _schema.location = cls._schema_network_security_group_read.location
            _schema.name = cls._schema_network_security_group_read.name
            _schema.properties = cls._schema_network_security_group_read.properties
            _schema.tags = cls._schema_network_security_group_read.tags
            _schema.type = cls._schema_network_security_group_read.type
            return

        cls._schema_network_security_group_read = _schema_network_security_group_read = AAZObjectType()

        network_security_group_read = _schema_network_security_group_read
        network_security_group_read.etag = AAZStrType()
        network_security_group_read.id = AAZStrType()
        network_security_group_read.location = AAZStrType()
        network_security_group_read.name = AAZStrType(
            flags={"read_only": True},
        )
        network_security_group_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        network_security_group_read.tags = AAZDictType()
        network_security_group_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_network_security_group_read.properties
        properties.default_security_rules = AAZListType(
            serialized_name="defaultSecurityRules",
        )
        properties.network_interfaces = AAZListType(
            serialized_name="networkInterfaces",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.resource_guid = AAZStrType(
            serialized_name="resourceGuid",
        )
        properties.security_rules = AAZListType(
            serialized_name="securityRules",
        )
        properties.subnets = AAZListType()

        default_security_rules = _schema_network_security_group_read.properties.default_security_rules
        default_security_rules.Element = AAZObjectType()
        cls._build_schema_security_rule_read(default_security_rules.Element)

        network_interfaces = _schema_network_security_group_read.properties.network_interfaces
        network_interfaces.Element = AAZObjectType()
        cls._build_schema_network_interface_read(network_interfaces.Element)

        security_rules = _schema_network_security_group_read.properties.security_rules
        security_rules.Element = AAZObjectType()
        cls._build_schema_security_rule_read(security_rules.Element)

        subnets = _schema_network_security_group_read.properties.subnets
        subnets.Element = AAZObjectType()
        cls._build_schema_subnet_read(subnets.Element)

        tags = _schema_network_security_group_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_network_security_group_read.etag
        _schema.id = cls._schema_network_security_group_read.id
        _schema.location = cls._schema_network_security_group_read.location
        _schema.name = cls._schema_network_security_group_read.name
        _schema.properties = cls._schema_network_security_group_read.properties
        _schema.tags = cls._schema_network_security_group_read.tags
        _schema.type = cls._schema_network_security_group_read.type

    _schema_public_ip_address_read = None

    @classmethod
    def _build_schema_public_ip_address_read(cls, _schema):
        if cls._schema_public_ip_address_read is not None:
            _schema.etag = cls._schema_public_ip_address_read.etag
            _schema.id = cls._schema_public_ip_address_read.id
            _schema.location = cls._schema_public_ip_address_read.location
            _schema.name = cls._schema_public_ip_address_read.name
            _schema.properties = cls._schema_public_ip_address_read.properties
            _schema.tags = cls._schema_public_ip_address_read.tags
            _schema.type = cls._schema_public_ip_address_read.type
            return

        cls._schema_public_ip_address_read = _schema_public_ip_address_read = AAZObjectType()

        public_ip_address_read = _schema_public_ip_address_read
        public_ip_address_read.etag = AAZStrType()
        public_ip_address_read.id = AAZStrType()
        public_ip_address_read.location = AAZStrType()
        public_ip_address_read.name = AAZStrType(
            flags={"read_only": True},
        )
        public_ip_address_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        public_ip_address_read.tags = AAZDictType()
        public_ip_address_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_public_ip_address_read.properties
        properties.dns_settings = AAZObjectType(
            serialized_name="dnsSettings",
        )
        properties.idle_timeout_in_minutes = AAZIntType(
            serialized_name="idleTimeoutInMinutes",
        )
        properties.ip_address = AAZStrType(
            serialized_name="ipAddress",
        )
        properties.ip_configuration = AAZObjectType(
            serialized_name="ipConfiguration",
        )
        cls._build_schema_ip_configuration_read(properties.ip_configuration)
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.public_ip_address_version = AAZStrType(
            serialized_name="publicIPAddressVersion",
        )
        properties.public_ip_allocation_method = AAZStrType(
            serialized_name="publicIPAllocationMethod",
        )
        properties.resource_guid = AAZStrType(
            serialized_name="resourceGuid",
        )

        dns_settings = _schema_public_ip_address_read.properties.dns_settings
        dns_settings.domain_name_label = AAZStrType(
            serialized_name="domainNameLabel",
        )
        dns_settings.fqdn = AAZStrType()
        dns_settings.reverse_fqdn = AAZStrType(
            serialized_name="reverseFqdn",
        )

        tags = _schema_public_ip_address_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_public_ip_address_read.etag
        _schema.id = cls._schema_public_ip_address_read.id
        _schema.location = cls._schema_public_ip_address_read.location
        _schema.name = cls._schema_public_ip_address_read.name
        _schema.properties = cls._schema_public_ip_address_read.properties
        _schema.tags = cls._schema_public_ip_address_read.tags
        _schema.type = cls._schema_public_ip_address_read.type

    _schema_security_rule_read = None

    @classmethod
    def _build_schema_security_rule_read(cls, _schema):
        if cls._schema_security_rule_read is not None:
            _schema.etag = cls._schema_security_rule_read.etag
            _schema.id = cls._schema_security_rule_read.id
            _schema.name = cls._schema_security_rule_read.name
            _schema.properties = cls._schema_security_rule_read.properties
            return

        cls._schema_security_rule_read = _schema_security_rule_read = AAZObjectType()

        security_rule_read = _schema_security_rule_read
        security_rule_read.etag = AAZStrType()
        security_rule_read.id = AAZStrType()
        security_rule_read.name = AAZStrType()
        security_rule_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_security_rule_read.properties
        properties.access = AAZStrType(
            flags={"required": True},
        )
        properties.description = AAZStrType()
        properties.destination_address_prefix = AAZStrType(
            serialized_name="destinationAddressPrefix",
            flags={"required": True},
        )
        properties.destination_port_range = AAZStrType(
            serialized_name="destinationPortRange",
        )
        properties.direction = AAZStrType(
            flags={"required": True},
        )
        properties.priority = AAZIntType()
        properties.protocol = AAZStrType(
            flags={"required": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.source_address_prefix = AAZStrType(
            serialized_name="sourceAddressPrefix",
            flags={"required": True},
        )
        properties.source_port_range = AAZStrType(
            serialized_name="sourcePortRange",
        )

        _schema.etag = cls._schema_security_rule_read.etag
        _schema.id = cls._schema_security_rule_read.id
        _schema.name = cls._schema_security_rule_read.name
        _schema.properties = cls._schema_security_rule_read.properties

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id

    _schema_subnet_read = None

    @classmethod
    def _build_schema_subnet_read(cls, _schema):
        if cls._schema_subnet_read is not None:
            _schema.etag = cls._schema_subnet_read.etag
            _schema.id = cls._schema_subnet_read.id
            _schema.name = cls._schema_subnet_read.name
            _schema.properties = cls._schema_subnet_read.properties
            return

        cls._schema_subnet_read = _schema_subnet_read = AAZObjectType()

        subnet_read = _schema_subnet_read
        subnet_read.etag = AAZStrType()
        subnet_read.id = AAZStrType()
        subnet_read.name = AAZStrType()
        subnet_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_subnet_read.properties
        properties.address_prefix = AAZStrType(
            serialized_name="addressPrefix",
        )
        properties.ip_configurations = AAZListType(
            serialized_name="ipConfigurations",
        )
        properties.network_security_group = AAZObjectType(
            serialized_name="networkSecurityGroup",
        )
        cls._build_schema_network_security_group_read(properties.network_security_group)
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.route_table = AAZObjectType(
            serialized_name="routeTable",
        )

        ip_configurations = _schema_subnet_read.properties.ip_configurations
        ip_configurations.Element = AAZObjectType()
        cls._build_schema_ip_configuration_read(ip_configurations.Element)

        route_table = _schema_subnet_read.properties.route_table
        route_table.etag = AAZStrType()
        route_table.id = AAZStrType()
        route_table.location = AAZStrType()
        route_table.name = AAZStrType(
            flags={"read_only": True},
        )
        route_table.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        route_table.tags = AAZDictType()
        route_table.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_subnet_read.properties.route_table.properties
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.routes = AAZListType()
        properties.subnets = AAZListType()

        routes = _schema_subnet_read.properties.route_table.properties.routes
        routes.Element = AAZObjectType()

        _element = _schema_subnet_read.properties.route_table.properties.routes.Element
        _element.etag = AAZStrType()
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_subnet_read.properties.route_table.properties.routes.Element.properties
        properties.address_prefix = AAZStrType(
            serialized_name="addressPrefix",
        )
        properties.next_hop_ip_address = AAZStrType(
            serialized_name="nextHopIpAddress",
        )
        properties.next_hop_type = AAZStrType(
            serialized_name="nextHopType",
            flags={"required": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )

        subnets = _schema_subnet_read.properties.route_table.properties.subnets
        subnets.Element = AAZObjectType()
        cls._build_schema_subnet_read(subnets.Element)

        tags = _schema_subnet_read.properties.route_table.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_subnet_read.etag
        _schema.id = cls._schema_subnet_read.id
        _schema.name = cls._schema_subnet_read.name
        _schema.properties = cls._schema_subnet_read.properties


__all__ = ["Show"]
