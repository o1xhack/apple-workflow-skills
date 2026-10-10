import SwiftUI
struct Payload { let title: String }
struct Sample: View {
 @State private var pending: Payload?
 var body: some View {
  Text("A").confirmationDialog("Confirm", item: $pending) { item in Button(item.title) {} } message: { item in Text(item.title) }
 }
}
