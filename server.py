from concurrent import futures
import logging

import grpc

import temperature_pb2
import temperature_pb2_grpc


class TemperatureServicer(temperature_pb2_grpc.TemperatureRecordingServicer):
    """Provides methods that implement functionality of route guide server."""

    def TemperatureMeasurementStats(self, recording, context):
        return temperature_pb2.TemperatureEntry(recording=recording.temperatureRecording, persisted=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    temperature_pb2_grpc.add_TemperatureRecordingServicer_to_server(TemperatureServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

