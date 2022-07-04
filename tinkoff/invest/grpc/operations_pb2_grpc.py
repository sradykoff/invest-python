# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from tinkoff.invest.grpc import operations_pb2 as tinkoff_dot_invest_dot_grpc_dot_operations__pb2


class OperationsServiceStub(object):
    """Сервис предназначен для получения:</br> **1**.  списка операций по счёту;</br> **2**.
    портфеля по счёту;</br> **3**. позиций ценных бумаг на счёте;</br> **4**.
    доступного остатка для вывода средств;</br> **4**. получения различных отчётов.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOperations = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OperationsService/GetOperations',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.OperationsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.OperationsResponse.FromString,
                )
        self.GetPortfolio = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OperationsService/GetPortfolio',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioResponse.FromString,
                )
        self.GetPositions = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OperationsService/GetPositions',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsResponse.FromString,
                )
        self.GetWithdrawLimits = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OperationsService/GetWithdrawLimits',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.WithdrawLimitsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.WithdrawLimitsResponse.FromString,
                )
        self.GetBrokerReport = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OperationsService/GetBrokerReport',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.BrokerReportRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.BrokerReportResponse.FromString,
                )
        self.GetDividendsForeignIssuer = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OperationsService/GetDividendsForeignIssuer',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetDividendsForeignIssuerRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetDividendsForeignIssuerResponse.FromString,
                )


class OperationsServiceServicer(object):
    """Сервис предназначен для получения:</br> **1**.  списка операций по счёту;</br> **2**.
    портфеля по счёту;</br> **3**. позиций ценных бумаг на счёте;</br> **4**.
    доступного остатка для вывода средств;</br> **4**. получения различных отчётов.
    """

    def GetOperations(self, request, context):
        """Метод получения списка операций по счёту.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPortfolio(self, request, context):
        """Метод получения портфеля по счёту.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPositions(self, request, context):
        """Метод получения списка позиций по счёту.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWithdrawLimits(self, request, context):
        """Метод получения доступного остатка для вывода средств.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBrokerReport(self, request, context):
        """Метод получения брокерского отчёта.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDividendsForeignIssuer(self, request, context):
        """Метод получения отчёта "Справка о доходах за пределами РФ".
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OperationsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOperations,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.OperationsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.OperationsResponse.SerializeToString,
            ),
            'GetPortfolio': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPortfolio,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioResponse.SerializeToString,
            ),
            'GetPositions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPositions,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsResponse.SerializeToString,
            ),
            'GetWithdrawLimits': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWithdrawLimits,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.WithdrawLimitsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.WithdrawLimitsResponse.SerializeToString,
            ),
            'GetBrokerReport': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBrokerReport,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.BrokerReportRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.BrokerReportResponse.SerializeToString,
            ),
            'GetDividendsForeignIssuer': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDividendsForeignIssuer,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetDividendsForeignIssuerRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetDividendsForeignIssuerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tinkoff.public.invest.api.contract.v1.OperationsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OperationsService(object):
    """Сервис предназначен для получения:</br> **1**.  списка операций по счёту;</br> **2**.
    портфеля по счёту;</br> **3**. позиций ценных бумаг на счёте;</br> **4**.
    доступного остатка для вывода средств;</br> **4**. получения различных отчётов.
    """

    @staticmethod
    def GetOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsService/GetOperations',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.OperationsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.OperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPortfolio(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsService/GetPortfolio',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPositions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsService/GetPositions',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetWithdrawLimits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsService/GetWithdrawLimits',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.WithdrawLimitsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.WithdrawLimitsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBrokerReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsService/GetBrokerReport',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.BrokerReportRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.BrokerReportResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDividendsForeignIssuer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsService/GetDividendsForeignIssuer',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetDividendsForeignIssuerRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetDividendsForeignIssuerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class OperationsStreamServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PortfolioStream = channel.unary_stream(
                '/tinkoff.public.invest.api.contract.v1.OperationsStreamService/PortfolioStream',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioStreamRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioStreamResponse.FromString,
                )


class OperationsStreamServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PortfolioStream(self, request, context):
        """Server-side stream обновлений портфеля
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OperationsStreamServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PortfolioStream': grpc.unary_stream_rpc_method_handler(
                    servicer.PortfolioStream,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioStreamRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioStreamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tinkoff.public.invest.api.contract.v1.OperationsStreamService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OperationsStreamService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PortfolioStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsStreamService/PortfolioStream',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioStreamRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
