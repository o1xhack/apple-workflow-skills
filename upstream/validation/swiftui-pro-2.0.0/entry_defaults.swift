import SwiftUI
import Foundation
class Store {}
extension EnvironmentValues {
 @Entry var store = Store()
 @Entry var token = UUID()
 @Entry var callback: () -> Void = {}
}
